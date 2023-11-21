package main

import "fmt"

func main() {
	nums := [10]int{}

	for i := range nums {
		number := i + 1
		if number%2 == 0 {
			fmt.Printf("%v is an even\n", number)
		} else {
			fmt.Printf("%v is an odd\n", number)
		}
	}
}
