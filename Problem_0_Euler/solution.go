package main

import "fmt"

func main() {
	sum := 0
	for i := 1; i <= 188000; i++ {
		square := i * i
		if square%2 == 1 {
			sum += square
		}
	}
	fmt.Println(sum)
}
