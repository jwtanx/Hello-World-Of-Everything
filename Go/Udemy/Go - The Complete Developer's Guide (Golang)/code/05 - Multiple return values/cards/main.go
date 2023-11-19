package main

func main() {
	cards := newDeck()
	hand, remainingCards := deal(cards, 5)
	// hand, remainingCards := cards.deal(5) // Both works the same

	hand.print()
	remainingCards.print()
}
