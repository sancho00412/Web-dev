package main

import "fmt"

func divMod(a, b int) (int, int) {
	return a / b, a % b
}

func main() {
	quotient, remainder := divMod(10, 3)
	fmt.Println("Quotient:", quotient, "Remainder:", remainder)
}
