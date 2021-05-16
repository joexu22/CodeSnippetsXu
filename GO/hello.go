package main

import (
	"fmt"
	"math/rand"
	"time"
	"rsc.io/quote"
)

func main() {
	rand.Seed(time.Now().UTC().UnixNano())
	fmt.Printf("Hello Go World!\n")
	fmt.Println("My favorite number is: ", rand.Intn(10))
	fmt.Println(quote.Go())
}
