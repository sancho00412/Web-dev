package main

import "fmt"

func main() {
	var a int = 10
	var b float64 = 20.5
	var name string = "Go Language"
	var isActive bool = true

	// Short declaration
	c := 30
	pi := 3.14
	greeting := "Hello"
	isCool := false

	fmt.Printf("a: %d, type: %T\n", a, a)
	fmt.Printf("b: %f, type: %T\n", b, b)
	fmt.Printf("name: %s, type: %T\n", name, name)
	fmt.Printf("isActive: %t, type: %T\n", isActive, isActive)
	fmt.Printf("c: %d, type: %T\n", c, c)
	fmt.Printf("pi: %f, type: %T\n", pi, pi)
	fmt.Printf("greeting: %s, type: %T\n", greeting, greeting)
	fmt.Printf("isCool: %t, type: %T\n", isCool, isCool)
}
