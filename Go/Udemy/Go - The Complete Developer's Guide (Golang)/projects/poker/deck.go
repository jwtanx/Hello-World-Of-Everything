package main

import "fmt"

type deck []string

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

func (d deck) print() {
	for _, card := range d {
		fmt.Println(card)
	}
}
