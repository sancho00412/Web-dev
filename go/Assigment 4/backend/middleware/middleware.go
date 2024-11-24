package middleware

import (
	"net/http"

	"github.com/gorilla/csrf"
)

var csrfMiddleware = csrf.Protect([]byte("32-byte-long-auth-key"), csrf.Secure(true))

func ApplyCSRFProtection(next http.Handler) http.Handler {
	return csrfMiddleware(next)
}
