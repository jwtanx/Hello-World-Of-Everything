package main

import "fmt"

func main() {
	// Function 1: Create a list of playing cards
	fmt.Println("\nFunction 1")
	cards := newDeck()

	// Function 2: Log out the content of the deck of cards
	fmt.Println("\nFunction 2")
	cards.print()

	// Function 3: Shuffle all cards in the deck
	fmt.Println("\nFunction 3")
	// cards := cards.shuffle()

	// Function 4: Create a hand of cards
	fmt.Println("\nFunction 4")
	draw, remaining := deal(cards, 5)

	// Function 5: Log out the cards in string
	fmt.Println("\nFunction 5")
	fmt.Println("Cards drew: " + draw.toString())
	fmt.Println("Remaining cards: " + remaining.toString())

	// Function 6: Saving to file
	fmt.Println("\nFunction 6")
	filename := "my_card"
	err := draw.saveToFile(filename)
	if err != nil {
		panic(err)
	} else {
		fmt.Println("File saved to " + filename)
	}

	// Function 7: Load a list of card from file
	fmt.Println("\nFunction 7")
	loadCards := newDeckFromFile(filename)
	loadCards.print()
}
