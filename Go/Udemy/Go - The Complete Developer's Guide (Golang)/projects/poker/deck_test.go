package main

import (
	"os"
	"testing"
)

// We will tell the variable t here if something went wrong
func TestNewDeck(t *testing.T) {
	cards := newDeck()

	// Test 1: Total number of cards
	totalDeckCards := 52
	if len(cards) != totalDeckCards {
		t.Errorf("Expected deck leng of %v, but got %v", totalDeckCards, len(cards))
	}
}

func TestSaveAndLoad(t *testing.T) {
	os.Remove("test_deck")

	deck := newDeck()
	deck.saveToFile("test_deck")

	newDeckFromFile("test_deck")

	os.Remove("test_deck")
}
