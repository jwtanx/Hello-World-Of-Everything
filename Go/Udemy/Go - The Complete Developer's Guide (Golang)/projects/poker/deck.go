package main

import (
	"fmt"
	"os"
	"strings"
)

type deck []string

// Function 1: Create a list of playing cards
func newDeck() deck {

	cards := deck{}
	suits := []string{"Spade", "Heart", "Club", "Diamond"}
	nums := []string{"A", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"}

	for _, suit := range suits {
		for _, num := range nums {
			cards = append(cards, num+" of "+suit)
		}
	}

	return cards
}

// Function 2: Log out the content of the deck of cards
func (d deck) print() {
	for _, card := range d {
		fmt.Println(card)
	}
}

// Function 3: Shuffle all cards in the deck
func (d deck) shuffle() deck {
	// WIP
	return d
}

// Function 4: Create a hand of cards
func deal(d deck, numOfCards int) (deck, deck) {
	draw := d[:numOfCards]
	remaining := d[numOfCards:]
	return draw, remaining
}

// Function 5: Log out the cards in string
func (d deck) toString() string {
	return strings.Join(d, ",")
}

// Function 6: Saving to file
func (d deck) saveToFile(filename string) error {
	err := os.WriteFile(filename, []byte(d.toString()), 0666)
	return err
}

// Function 7: Load a list of card from file
func newDeckFromFile(filename string) deck {
	bs, err := os.ReadFile(filename)
	if err != nil {
		panic(err)
	}
	return deck(strings.Split(string(bs), ","))
}
