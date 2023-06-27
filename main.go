package main

import (
	"fmt"
	"strings"
)

func main() {
  str1 := "educative.io"
	fmt.Println(str1, "io", strings.Contains(str1, "io"))
	fmt.Println(str1, "shot", strings.Contains(str1, "shot"))
	fmt.Println(str1, "", strings.Contains(str1, ""))

	var s string = "Hello, World"
  
	for index, character := range(s){
	  fmt.Printf("The character %c is in position %d \n", character, index)
	}
}