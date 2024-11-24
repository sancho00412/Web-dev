package handlers

import (
	"backend/validators"
	"encoding/json"
	"net/http"
)

func RegisterHandler(w http.ResponseWriter, r *http.Request) {
	var user struct {
		Email string `json:"email"`
		Age   int    `json:"age"`
	}
	err := json.NewDecoder(r.Body).Decode(&user)
	if err != nil {
		http.Error(w, "Invalid request body", http.StatusBadRequest)
		return
	}

	if err := validators.ValidateEmail(user.Email); err != nil {
		http.Error(w, "Invalid email format", http.StatusBadRequest)
		return
	}
	if err := validators.ValidateAge(user.Age); err != nil {
		http.Error(w, "Age must be 18 or older", http.StatusBadRequest)
		return
	}

	w.Write([]byte("User registered successfully"))
}
