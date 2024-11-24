package validators

import (
	"github.com/go-playground/validator/v10"
)

var validate = validator.New()

func ValidateEmail(email string) error {
	return validate.Var(email, "required,email")
}

func ValidateAge(age int) error {
	return validate.Var(age, "gte=18")
}
