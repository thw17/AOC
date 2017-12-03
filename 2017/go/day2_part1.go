/*
2017 AOC Day 2 Part 1 Corruption Checksum

Calculate a file's checksum using the following algorithm. For each row,
determine the difference between the largest and smallest value and then
sum all of the differences.


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

	var diff int
	sum := 0

	for scanner.Scan() {
		s := strings.Split(scanner.Text(), "\t")

		init_i, err := strconv.Atoi(s[0])
		if err != nil {
			panic(err)
		}
		var max int = init_i
		var min int = init_i
		for _, val := range s {
			iConv, err := strconv.Atoi(val)
			if err != nil {
				panic (err)
			}
			if iConv > max {
				max = iConv
			} else if iConv < min {
				min = iConv
			}
		}

		diff = max - min
		sum += diff
	}

	fmt.Println(sum)
}
