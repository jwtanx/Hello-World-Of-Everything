package main

import "fmt"

type deck []string

func newDeck() deck {
	cards := deck{}

	cardSuits := []string{"Spades", "Diamonds", "Hearts", "Clubs"}
	cardValues := []string{"Ace", "Two", "Three", "Four"}

	for _, suit := range cardSuits {
		for _, value := range cardValues {
			cards = append(cards, value+" of "+suit)
		}
	}
	return cards

}

func (d deck) print() {
	for i, card := range d {
		fmt.Println(i, card)
	}
}

// In main.go: hand, remainingCards := deal(cards, 5)
func deal(d deck, handSize int) (deck, deck) {
	return d[:handSize], d[handSize:]
}

// In main.go: hand, remainingCards := cards.deal(5)
// There is specified use case for this, in this case we use the method above rather than receiving function
// If we are using the receiver method, it feel like the variable deck d is modified
// func (d deck) deal(handSize int) (deck, deck) {
// 	return d[:handSize], d[handSize:]
// }
