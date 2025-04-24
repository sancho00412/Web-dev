// cmd/main.go
package main

import (
	"database/sql"
	"log"
	"net/http"
	"onlinestore/internal/handlers"
	"onlinestore/pkg/cart"
	"onlinestore/pkg/category"
	"onlinestore/pkg/order"
	"onlinestore/pkg/payment"
	"onlinestore/pkg/product"
	"onlinestore/pkg/review"
	"onlinestore/pkg/user"

	"github.com/gorilla/mux"
	_ "github.com/lib/pq"
	"github.com/rs/cors"
)

func DeleteProduct(db *sql.DB) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		vars := mux.Vars(r)
		productID := vars["id"]

		// Проверка, что ID не пустой
		if productID == "" {
			http.Error(w, "ID товара не найден", http.StatusBadRequest)
			return
		}

		// Выполнение запроса для удаления товара
		res, err := db.Exec("DELETE FROM products WHERE id = $1", productID)
		if err != nil {
			log.Println("Ошибка при удалении товара:", err)
			http.Error(w, "Ошибка при удалении товара", http.StatusInternalServerError)
			return
		}

		// Проверка, был ли удален товар
		rowsAffected, err := res.RowsAffected()
		if err != nil || rowsAffected == 0 {
			http.Error(w, "Товар не найден", http.StatusNotFound)
			return
		}

		w.WriteHeader(http.StatusOK)
		w.Write([]byte("Товар успешно удален"))
	}
}

func main() {
	db, err := sql.Open("postgres", "postgres://postgres:sanat@localhost/os?sslmode=disable")

	if err != nil {
		log.Fatal(err)
	}
	defer db.Close()

	err = category.EnsureCategoryTableExists(db)
	if err != nil {
		log.Fatal(err)
	}

	categories := []category.Category{
		{Name: "Home Appliances"},
		{Name: "Phones"},
		{Name: "End Devices"},
	}

	err = category.InsertInitialCategories(db, categories)
	if err != nil {
		log.Fatal(err)
	}

	err = product.EnsureTableExists(db)
	if err != nil {
		log.Fatal(err)
	}

	products := []product.Product{
		{Name: "Набор гантелей SHYN SPORT", Price: 12500, Description: "Product Description 1", QuantityInStock: 12, ImagePath: "https://resources.cdn-kaspi.kz/img/m/p/h90/ha1/86243885056030.jpg?format=gallery-medium", CategoryID: 2},
		{Name: "Ролик для пресса ART FiT", Price: 6500, Description: "Product Description 2", QuantityInStock: 3, ImagePath: "https://resources.cdn-kaspi.kz/img/m/p/h72/h28/82828382273566.jpg?format=gallery-medium", CategoryID: 2},
		{Name: "Скакалка SUNLIN", Price: 2000, Description: "Product Description 3", QuantityInStock: 1, ImagePath: "https://resources.cdn-kaspi.kz/img/m/p/hc8/hff/68309702115358.jpg?format=gallery-medium", CategoryID: 2},
		{Name: "Гиря Genau Best Kettelbell", Price: 70000, Description: "Product Description 4", QuantityInStock: 2, ImagePath: "https://resources.cdn-kaspi.kz/img/m/p/p94/pe2/8208789.jpg?format=gallery-medium", CategoryID: 2},
		{Name: "Боксерские перчатки", Price: 6500, Description: "Product Description 5", QuantityInStock: 12, ImagePath: "https://resources.cdn-kaspi.kz/img/m/p/he6/h2a/69753084674078.jpg?format=gallery-medium", CategoryID: 2},
	}

	err = product.InsertInitialProducts(db, products)
	if err != nil {
		log.Fatal(err)
	}

	err = user.EnsureUserTableExists(db)
	if err != nil {
		log.Fatal(err)
	}

	err = cart.EnsureCartTableExists(db)
	if err != nil {
		log.Fatal(err)
	}

	err = order.EnsureOrderTableExists(db)
	if err != nil {
		log.Fatal(err)
	}

	err = payment.EnsurePaymentInfoTableExists(db)
	if err != nil {
		log.Fatal(err)
	}

	err = review.EnsureReviewTableExists(db)
	if err != nil {
		log.Fatal(err)
	}

	r := mux.NewRouter()

	r.HandleFunc("/api/register", func(w http.ResponseWriter, r *http.Request) {
		handlers.RegisterHandler(w, r, db)
	}).Methods("POST")

	r.HandleFunc("/api/login", func(w http.ResponseWriter, r *http.Request) {
		handlers.LoginHandler(w, r, db)
	}).Methods("POST")

	r.HandleFunc("/api/logout", func(w http.ResponseWriter, r *http.Request) {
		handlers.LogoutHandler(w, r, db)
	}).Methods("POST")

	r.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		handlers.HomeHandler(w, r, db)
	}).Methods("GET")

	r.HandleFunc("/api/products", handlers.GetAllProducts(db)).Methods("GET")
	r.HandleFunc("/api/products/{id}", handlers.GetProductByID(db)).Methods("GET")
	r.HandleFunc("/api/products", handlers.CreateProduct(db)).Methods("POST")
	r.HandleFunc("/api/products/{id}", handlers.UpdateProduct(db)).Methods("PUT")
	r.HandleFunc("/api/products/{id}", handlers.DeleteProduct(db)).Methods("DELETE")

	r.HandleFunc("/api/products/{id}/review", handlers.CreateProductReview(db)).Methods("POST")
	r.HandleFunc("/api/products/{id}/review", handlers.GetProductReviews(db)).Methods("GET")

	r.HandleFunc("/api/products/{id}/cart", handlers.AddToCartForProduct(db)).Methods("POST")

	r.HandleFunc("/api/cart", handlers.GetCartItemsHandler(db)).Methods("GET")
	r.HandleFunc("/api/cart/{product_id}", handlers.AddToCart(db)).Methods("POST")
	r.HandleFunc("/api/cart/{product_id}", handlers.RemoveFromCart(db)).Methods("DELETE")

	r.HandleFunc("/api/payments", handlers.GetAllPaymentsForCurrentUser(db)).Methods("GET")
	r.HandleFunc("/api/payments/{id}", handlers.GetPaymentByID(db)).Methods("GET")
	r.HandleFunc("/api/payments", handlers.CreatePayment(db)).Methods("POST")

	r.HandleFunc("/api/orders", func(w http.ResponseWriter, r *http.Request) {
		handlers.PostOrderHandler(w, r, db)
	}).Methods("POST")
	r.HandleFunc("/api/orders", func(w http.ResponseWriter, r *http.Request) {
		handlers.GetOrdersHandler(w, r, db)
	}).Methods("GET")
	r.HandleFunc("/api/orders/{id}", func(w http.ResponseWriter, r *http.Request) {
		handlers.GetOrderHandler(w, r, db)
	}).Methods("GET")

	r.HandleFunc("/api/orders/{id}/payment", handlers.CreatePaymentForOrder(db)).Methods("POST")

	r.HandleFunc("/api/profile", handlers.ProfileHandler(db)).Methods("GET")

	r.HandleFunc("/api/categories", handlers.GetAllCategories(db)).Methods("GET")
	r.HandleFunc("/api/categories/{id}", handlers.GetCategoryByID(db)).Methods("GET")
	r.HandleFunc("/api/categories", handlers.CreateCategory(db)).Methods("POST")
	r.HandleFunc("/api/categories/{id}", handlers.UpdateCategory(db)).Methods("PUT")
	r.HandleFunc("/api/categories/{id}", handlers.DeleteCategory(db)).Methods("DELETE")

	r.HandleFunc("/api/categories/{id}/products", handlers.GetProductsByCategoryID(db)).Methods("GET")

	r.HandleFunc("/api/products/pagination/", func(w http.ResponseWriter, r *http.Request) {
		handlers.GetPaginatedProductsHandler(w, r, db)
	}).Methods("GET")

	r.HandleFunc("/api/products/sort/", func(w http.ResponseWriter, r *http.Request) {
		handlers.GetSortedProductsHandler(w, r, db)
	}).Methods("GET")

	r.HandleFunc("/api/products/filter/", func(w http.ResponseWriter, r *http.Request) {
		handlers.GetFilteredProductsHandler(w, r, db)
	}).Methods("GET")

	// Protected routes

	c := cors.New(cors.Options{
		AllowedOrigins:   []string{"http://localhost:4200"},
		AllowCredentials: true,
		AllowedMethods:   []string{"GET", "POST", "PUT", "DELETE"},
	})

	handler := c.Handler(r)

	log.Println("Server is running on port 8080...")
	if err := http.ListenAndServe(":8080", handler); err != nil {
		log.Fatal(err)
	}

}
