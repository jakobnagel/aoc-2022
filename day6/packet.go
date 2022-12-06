package main

import (
	"fmt"
	"os"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func main() {
	data, err := os.ReadFile("input.txt")
	check(err)

	for i := 13; i < len(data); i++ {
		piece := data[i-13 : i+1]
		if !hasDuplicate(piece) {
			println("First marker after character: " + fmt.Sprint(i+1))
			break
		}
	}
	fmt.Println("Hello World!")
}

func hasDuplicate(data []byte) bool {
	for i := 0; i < len(data); i++ {
		for j := i + 1; j < len(data); j++ {
			if data[i] == data[j] {
				return true
			}
		}
	}

	return false
}
