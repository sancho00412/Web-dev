package handlers

import (
	"database/sql"
	"encoding/json"
	"net/http"
	"onlinestore/pkg/review"

	"strconv"

	"github.com/gorilla/mux"
)

func CreateProductReview(db *sql.DB) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		var newReview review.Review
		err := json.NewDecoder(r.Body).Decode(&newReview)
		if err != nil {
			http.Error(w, "Invalid data format", http.StatusBadRequest)
			return
		}

		params := mux.Vars(r)
		productID, err := strconv.Atoi(params["id"])
		if err != nil {
			http.Error(w, "Invalid product ID", http.StatusBadRequest)
			return
		}

		newReview.ProductID = productID

		userID := getCurrentUserIDFromContextOrSession(r)
		if userID == 0 {
			http.Error(w, "Unauthorized", http.StatusUnauthorized)
			return
		}

		err = review.InsertProductReviewToDB(db, newReview, userID)
		if err != nil {
			http.Error(w, "Error adding product review", http.StatusInternalServerError)
			return
		}

		w.WriteHeader(http.StatusCreated)
	}
}

func GetProductReviews(db *sql.DB) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		params := mux.Vars(r)
		productID, err := strconv.Atoi(params["id"])
		if err != nil {
			http.Error(w, "Invalid product ID", http.StatusBadRequest)
			return
		}

		reviews, err := review.GetProductReviewsFromDB(db, productID)
		if err != nil {
			http.Error(w, "Error retrieving product reviews", http.StatusInternalServerError)
			return
		}

		w.Header().Set("Content-Type", "application/json")
		json.NewEncoder(w).Encode(reviews)
	}
}
