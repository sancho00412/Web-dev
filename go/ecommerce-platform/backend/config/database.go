package config

import (
	"log"

	"gorm.io/driver/postgres"
	"gorm.io/gorm"
)

// DB - глобальная переменная для подключения к базе данных
var DB *gorm.DB

// ConnectDatabase - функция подключения к базе данных
func ConnectDatabase() {
	dsn := "host=localhost user=postgres password=sanat dbname=os port=5432 sslmode=disable"
	database, err := gorm.Open(postgres.Open(dsn), &gorm.Config{})
	if err != nil {
		log.Fatal("Failed to connect to the database:", err)
	}

	DB = database
	log.Println("Database connected successfully!")
}
