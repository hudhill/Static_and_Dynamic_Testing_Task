import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    
    def setUp(self):
        self.card1 = Card("Spades", 9)
        self.card2 = Card("Diamonds", 1)
        self.card3 = Card("Hearts", 12)

        self.card_game = CardGame()

    def test_check_for_ace(self):
        self.assertEqual(False, self.card_game.check_for_ace(self.card1))
        self.assertEqual(True, self.card_game.check_for_ace(self.card2))

    def test_highest_card(self):
        self.assertEqual(self.card3, self.card_game.highest_card(self.card1, self.card3))

    def test_cards_total(self):
        cards = [self.card1, self.card2, self.card3]
        self.assertEqual("You have a total of 22", self.card_game.cards_total(cards))
