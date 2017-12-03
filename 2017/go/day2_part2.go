/*
2017 AOC Day 2 Part 2 Corruption Checksum

Calculate a file's checksum using the following algorithm. Find the only two
numbers in each row where one evenly divides the other, divide them, and add
up the result from all lines.


*/

package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {

	inputFile := os.Args[1]

	f, err := os.Open(inputFile)
	if err != nil {
		panic(err)
	}
	defer f.Close()
	scanner := bufio.NewScanner(f)

	sum := 0

	for scanner.Scan() {
		s := strings.Split(scanner.Text(), "\t")
		for idx, val := range s {
			intVal, err := strconv.Atoi(val)
			if err != nil {
				panic(err)
			}
			for _, comp := range s[idx + 1:] {
				intComp, err := strconv.Atoi(comp)
				if err != nil {
					panic(err)
				}
				if intVal % intComp == 0 {
					sum += intVal / intComp
					break
				} else if intComp % intVal == 0 {
					sum += intComp / intVal
					break
				}
			}
		}
	}

	fmt.Println(sum)
}
