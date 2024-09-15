package main

import "fmt"

func swap(a, b string) (string, string) {
	return b, a
}

func main() {
	first, second := swap("hello", "world")
	fmt.Println("Swapped:", first, second)
}
