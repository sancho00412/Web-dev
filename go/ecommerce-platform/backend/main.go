package main

import (
	"log"
	"net/http"

	"ecommerce-platform/config"

	"github.com/gorilla/mux"
)

func main() {
	// Подключаем базу данных
	config.ConnectDatabase()

	// Создаем маршрутизатор
	router := mux.NewRouter()

	// Пример маршрута
	router.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		w.Write([]byte("Welcome to the E-Commerce Platform!"))
	})

	// Запускаем сервер
	log.Println("Server is running on http://localhost:8080")
	log.Fatal(http.ListenAndServe(":8080", router))
}
