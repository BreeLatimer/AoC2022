package main

import (
	"bufio"
	"container/list"
	"log"
	"os"
	"strconv"
)

func main() {
	// Read calorie_input.txt
	file, err := os.Open("calorie_input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	// Create an of elves
	elves := list.New()

	elfCalorieTotal := 0

	// Read file line by line
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		// Convert string to int
		if scanner.Text() == "" {
			// Create a new elf, and go to the next elf
			elves.PushBack(elfCalorieTotal)
			elfCalorieTotal = 0
		} else {
			calorie, err := strconv.Atoi(scanner.Text())
			if err != nil {
				log.Fatal(err)
			}

			// Add calorie to elves
			elfCalorieTotal += calorie
		}
	}

	// Print the maximum number in the list
	max := 0
	for e := elves.Front(); e != nil; e = e.Next() {
		if e.Value.(int) > max {
			max = e.Value.(int)
		}
	}
	log.Println(max)
}
