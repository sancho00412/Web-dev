// pkg/auth/auth.go

package auth

import (
	"database/sql"
	"errors"
	"net/http"
	"onlinestore/pkg/user"
	"strings"

	"time"

	"github.com/dgrijalva/jwt-go"
)

var secretKey = []byte("secret") // Секретный ключ для подписи токена

type Claims struct {
	UserID   int    `json:"user_id"`
	Username string `json:"username"`
	jwt.StandardClaims
}

type Credentials struct {
	Username string `json:"username"`
	Password string `json:"password"`
}

func GenerateToken(userID int, username string) (string, error) {
	expirationTime := time.Now().Add(24 * time.Hour)

	claims := &Claims{
		UserID:   userID,
		Username: username,
		StandardClaims: jwt.StandardClaims{
			ExpiresAt: expirationTime.Unix(),
		},
	}

	token := jwt.NewWithClaims(jwt.SigningMethodHS256, claims)
	signedToken, err := token.SignedString(secretKey)
	if err != nil {
		return "", err
	}

	return signedToken, nil
}

func ParseToken(tokenString string) (*Claims, error) {
	token, err := jwt.ParseWithClaims(tokenString, &Claims{}, func(token *jwt.Token) (interface{}, error) {
		return secretKey, nil
	})
	if err != nil {
		return nil, err
	}

	claims, ok := token.Claims.(*Claims)
	if !ok || !token.Valid {
		return nil, errors.New("invalid token")
	}

	return claims, nil
}

func Login(credentials Credentials, db *sql.DB) (string, error) {

	user, err := GetUserByUsername(credentials.Username, db)
	if err != nil {
		return "", err
	}

	if user.Password != credentials.Password {
		return "", errors.New("incorrect username or password")
	}

	token, err := GenerateToken(user.ID, user.Username)
	if err != nil {
		return "", err
	}

	return token, nil
}

func GetUserByUsername(username string, db *sql.DB) (*user.User, error) {

	var u user.User
	err := db.QueryRow("SELECT id, username, email, password FROM users WHERE username = $1", username).Scan(&u.ID, &u.Username, &u.Email, &u.Password)
	if err != nil {

		if err == sql.ErrNoRows {
			return nil, errors.New("user not found")
		}

		return nil, err
	}

	return &u, nil
}

func UpdateUserToken(userID int, token string, db *sql.DB) error {

	_, err := db.Exec("UPDATE users SET token = $1 WHERE id = $2", token, userID)
	if err != nil {
		return err
	}
	return nil
}

func ExtractToken(r *http.Request) (string, error) {

	tokenString := r.Header.Get("Authorization")
	if tokenString == "" {
		return "", errors.New("token is missing")
	}

	tokenString = strings.Replace(tokenString, "Bearer ", "", 1)

	return tokenString, nil
}
