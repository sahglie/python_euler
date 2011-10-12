#!/opt/local/bin/python

"""In the card game poker, a hand consists of five cards and are ranked,
from lowest to highest, in the following way:

* High Card: Highest value card.
* One Pair: Two cards of the same value.
* Two Pairs: Two different pairs.
* Three of a Kind: Three cards of the same value.
* Straight: All cards are consecutive values.
* Flush: All cards of the same suit.
* Full House: Three of a kind and a pair.
* Four of a Kind: Four cards of the same value.
* Straight Flush: All cards are consecutive values of same suit.
* Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the highest
value wins; for example, a pair of eights beats a pair of fives (see example
1 below). But if two ranks tie, for example, both players have a pair of
queens, then highest cards in each hand are compared (see example 4 below); if
the highest cards tie then the next highest cards are compared, and so on.

Consider the following five hands dealt to two players:

Hand	 	Player 1	 	Player 2	 	Winner
1	 	5H 5C 6S 7S KD          2C 3S 8S 8D TD          Player 2
                Pair of Fives           Pair of Eights
 	
2	 	5D 8C 9S JS AC          2C 5C 7D 8S QH          Player 1
                Highest card Ace        Highest card Queen
 	
3	 	2D 9C AS AH AC          3D 6D 7D TD QD          Player 2
                Three Aces              Flush with Diamonds
 	
4	 	4D 6S 9H QH QC          3D 6D 7H QD QS          Player 1
                Pair of Queens          Pair of Queens
                Highest card Nine       Highest card Seven

5	 	2H 2D 4C 4D 4S          3C 3D 3S 9S 9D          Player 1
                Full House              Full House
                With Three Fours        with Three Threes


The file, poker.txt, contains one-thousand random hands dealt to two players.
Each line of the file contains ten cards (separated by a single space): the
first five are Player 1's cards and the last five are Player 2's cards. You
can assume that all hands are valid (no invalid characters or repeated cards),
each player's hand is in no specific order, and in each hand there is a clear
winner.

How many hands does Player 1 win?
"""

import unittest
from pdb import set_trace


class Hand:
    CARDS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14"]
    SUITS = set(["C", "D", "H", "S"])
    HIGH_CARD_MAPPING = {"T":"10", "J":"11", "Q":"12", "K":"13", "A":"14"}
    
    def __init__(self, cards):
        for m in self.HIGH_CARD_MAPPING:
            for i, card in enumerate(tuple(cards)):
                if card.startswith(m):
                    cards[i] = card.replace(m, self.HIGH_CARD_MAPPING[m])

        def card_sort_key(x):
            return int(self.rank(x))
        
        cards.sort(key=card_sort_key)
        self.cards = tuple(cards)

    def score(self):
        if self.royal_flush():
            return self.score_royal_flush()
        elif self.straight_flush():
            return self.score_straight_flush()
        elif self.four_of_a_kind():
            return self.score_four_of_a_kind()
        elif self.full_house():
            return self.score_full_house()
        elif self.flush():
            return self.score_flush()
        elif self.straight():
            return self.score_straight()
        elif self.three_of_a_kind():
            return self.score_three_of_a_kind()
        elif self.two_pairs():
            return self.score_two_pairs()
        elif self.one_pair():
            return self.score_one_pair()
        else:
            return 0

    def __cmp__(self, other):
        if self.score() < other.score():
            return -1
        elif self.score() > other.score():
            return 1
        else:
            n = 1
            while True:
                if self.highest_card_rank(n) < other.highest_card_rank(n):
                    return -1
                elif self.highest_card_rank(n) > other.highest_card_rank(n):
                    return 1
                n += 1

    def royal_flush(self):
        """Royal Flush: Ten, Jack, Queen, King, Ace, in same suit."""
        return self.flush() and \
               set(map(self.rank, self.cards)) == { "10", "11", "12", "13", "14" }

    def straight_flush(self):
        """Straight Flush: All cards are consecutive values of same suit."""
        return self.straight() and self.flush()

    def four_of_a_kind(self):
        """Four of a Kind: Four cards of the same value."""
        return self.__n_pairs(4, self.cards) > -1

    def full_house(self):
        """Full House: Three of a kind and a pair."""
        cards = list(self.cards)
        index = self.__n_pairs(3, cards)
        if index > -1:
            for i in range(index, index+3):
                cards.pop(index)
            return self.__n_pairs(2, cards) > -1
        else:
            return False
    
    def flush(self):
        """Flush: All cards of the same suit."""
        for s in self.SUITS:
            if all(map(lambda x: self.suit(x) == s, self.cards)):
                return True
        return False
    
    def straight(self):
        """Straight: All cards are consecutive values."""
        values = map(int, map(self.rank, self.cards))
        equalized = [values[0], values[1]-1, values[2]-2, values[3]-3, values[4]-4]
        return equalized.count(values[0]) == 5

    def three_of_a_kind(self):
        """Three of a Kind: Three cards of the same value."""
        return self.__n_pairs(3, self.cards) > -1

    def two_pairs(self):
        """Two Pairs: Two different pairs."""
        cards = list(self.cards)
        index = self.__n_pairs(2, cards)
        if index > -1:
            cards = cards[index+2:]
            return self.__n_pairs(2, cards) > -1
        else:
            return False
    
    def one_pair(self):
        """One Pair: Two cards of the same value."""
        return self.__n_pairs(2, self.cards) > -1
    
    def highest_card_rank(self, n = 1):
        return map(self.rank, list(set(self.cards)))[n]

    def suit(self, card):
        return card[-1:]

    def rank(self, card):
        return card[:-1]

    def score_royal_flush(self):
        return self.__sum_cards_rank(self.cards)

    def score_straight_flush(self):
        return self.__sum_cards_rank(self.cards) + 2

    def score_four_of_a_kind(self):
        index = self.__n_pairs(4, self.cards)
        return self.__sum_cards_rank(self.cards[index:index+4])

    def score_full_house(self):
        index = self.__n_pairs(3, self.cards)
        three = self.cards[index:index+3]
        remaining_cards = self.cards[index+3:]
        index = self.__n_pairs(2, remaining_cards)
        pair = remaining_cards[index:index+2]
        return self.__sum_cards_rank(three+pair) + 14

    def score_flush(self):
        return self.__sum_cards_rank(self.cards)
    
    def score_straight(self):
        return self.__sum_cards_rank(self.cards) - 7
        
    def score_three_of_a_kind(self):
        index = self.__n_pairs(3, self.cards)
        return self.__sum_cards_rank(self.cards[index:index+3])

    def score_two_pairs(self):
        index = self.__n_pairs(2, self.cards)
        pair1 = self.cards[index:index+2]
        remaining_cards = self.cards[index+2:]
        index = self.__n_pairs(2, remaining_cards)
        pair2 = remaining_cards[index:index+2]
        return self.__sum_cards_rank(pair1+pair2) - 13

    def score_one_pair(self):
        index = self.__n_pairs(2, self.cards)
        return self.__sum_cards_rank(self.cards[index:index+2])

    def __n_pairs(self, n, cards):
        values = map(self.rank, cards)
        for i, rank in enumerate(values):
            if values.count(rank) >= n:
                return i
        return -1

    def __sum_cards_rank(self, cards):
        return sum(map(lambda x: int(self.rank(x)), cards))


class TestHandRecognition(unittest.TestCase):
    def test_flush(self):
        self.assertTrue(Hand(["10C", "2C", "QC", "KC", "AC"]).flush())
        self.assertFalse(Hand(["10C", "JH", "QS", "KC", "AC"]).flush())
    
    def test_royal_flush(self):
        self.assertTrue(Hand(["10C", "JC", "QC", "KC", "AC"]).royal_flush())
        self.assertFalse(Hand(["10C", "JH", "QS", "KC", "AC"]).royal_flush())

    def test_straight_flush(self):
        self.assertTrue(Hand(["2C", "3C", "4C", "5C", "6C"]).straight_flush())
        self.assertFalse(Hand(["2C", "3H", "4S", "5C", "6C"]).straight_flush())

    def test_full_house(self):
        self.assertTrue(Hand(["2C", "2D", "2H", "5C", "5D"]).full_house())

    def test_four_of_a_kind(self):
        self.assertTrue(Hand(["2C", "2S", "2D", "2H", "AC"]).four_of_a_kind())
        self.assertFalse(Hand(["3C", "JH", "QS", "KC", "AC"]).four_of_a_kind())

    def test_three_of_a_kind(self):
        self.assertTrue(Hand(["2C", "2S", "2D", "KC", "AC"]).three_of_a_kind())
        self.assertFalse(Hand(["3C", "JH", "QS", "KC", "AC"]).three_of_a_kind())

    def test_straight(self):
        self.assertTrue(Hand(["2C", "3S", "4D", "5C", "6C"]).straight())
        self.assertTrue(Hand(["10C", "JH", "QS", "KC", "AC"]).straight())     
        self.assertFalse(Hand(["3C", "JH", "QS", "KC", "AC"]).straight())

    def test_one_pair(self):
        self.assertTrue(Hand(["2C", "2S", "4D", "5C", "6C"]).one_pair())
        self.assertFalse(Hand(["10C", "JH", "QS", "KC", "AC"]).one_pair())    

    def test_two_pair(self):
        self.assertTrue(Hand(["2C", "2S", "2D", "2H", "6C"]).two_pairs())
        self.assertFalse(Hand(["10C", "JH", "QS", "KC", "AC"]).two_pairs())   

    def test_highest_card_rank(self):
        self.assertEquals("6", Hand(["2C", "2S", "2D", "2H", "6C"]).highest_card_rank(1))
        self.assertEquals("2", Hand(["2C", "2S", "2D", "2H", "6C"]).highest_card_rank(2))


class TestHandScore(unittest.TestCase):
    def setUp(self):
        self.royal_flush = Hand(["TC", "JC", "QC", "KC", "AC"])
        self.straight_flush = Hand(["9C", "TC", "JC", "QC", "KC"])
        self.four_of_a_kind = Hand(["9C", "AH", "AS", "AD", "AC"])
        self.full_house = Hand(["KC", "KD", "AD", "AS", "AC"])
        self.flush = Hand(["8C", "TC", "JC", "QC", "KC"])
        self.straight = Hand(["TD", "JS", "QC", "KH", "AC"])
        self.three_of_a_kind = Hand(["8H", "TD", "AS", "AC", "AD"])
        self.two_pairs = Hand(["8H", "KD", "KS", "AC", "AD"])
        self.one_pair = Hand(["3H", "1D", "5S", "AC", "AD"])

    def test_hands(self):
        self.assertTrue(self.royal_flush.royal_flush())
        self.assertTrue(self.straight_flush.straight_flush())
        self.assertTrue(self.four_of_a_kind.four_of_a_kind())
        self.assertTrue(self.full_house.full_house())
        self.assertTrue(self.flush.flush())
        self.assertTrue(self.straight.straight())
        self.assertTrue(self.three_of_a_kind.three_of_a_kind())
        self.assertTrue(self.two_pairs.two_pairs())
        self.assertTrue(self.one_pair.one_pair())
        
    def test_royal_flush_always_wins(self):
        self.assertTrue(self.royal_flush > self.straight_flush,
                        "%s > %s" % (self.royal_flush.score(), self.straight_flush.score()))
        self.assertTrue(self.straight_flush > self.four_of_a_kind,
                        "%s > %s" % (self.straight_flush.score(), self.four_of_a_kind.score()))
        self.assertTrue(self.four_of_a_kind > self.full_house,
                        "%s > %s" % (self.four_of_a_kind.score(), self.full_house.score()))
        self.assertTrue(self.full_house > self.flush,
                        "%s > %s" % (self.full_house.score(), self.flush.score()))
        self.assertTrue(self.flush > self.straight,
                        "%s > %s" % (self.flush.score(), self.straight.score()))
        self.assertTrue(self.straight > self.three_of_a_kind,
                        "%s > %s" % (self.straight.score(), self.three_of_a_kind.score()))
        self.assertTrue(self.three_of_a_kind > self.two_pairs,
                        "%s > %s" % (self.three_of_a_kind.score(), self.two_pairs.score()))
        self.assertTrue(self.two_pairs > self.one_pair,
                        "%s > %s" % (self.two_pairs.score(), self.one_pair.score()))

class TestWins(unittest.TestCase):
    def test_hands(self):
        pair_of_fives = Hand(["5H", "5C", "6S", "7S", "KD"])
        pair_of_eights = Hand(["2C", "3S", "8S", "8D", "TD"])
        self.assertTrue(pair_of_eights > pair_of_fives)

        highest_card_ace = Hand(["5D", "8C", "9S", "JS", "AC"])
        highest_card_queen = Hand(["2C", "5C", "7D", "8S", "QH"])
        self.assertTrue(highest_card_ace > highest_card_queen)

        # three_aces = Hand(["2D", "9C", "AS", "AH", "AC"])
        # flush_w_diamonds = Hand(["3D", "6D", "7D", "TD", "QD"])
        # self.assertTrue(flush_w_diamonds > three_aces)

        pair_of_queens_high_card_nine = Hand(["4D", "6S", "9H", "QH", "QC"])
        pair_of_queens_high_card_seven = Hand(["3D", "6D", "7H", "QD", "QS"])
        self.assertTrue(pair_of_queens_high_card_nine > pair_of_queens_high_card_seven)

        full_house_w_fours = Hand(["2H", "2D", "4C", "4D", "4S"])
        full_house_w_threes = Hand(["3C", "3D", "3S", "9S", "9D"])
        full_house_w_fours > full_house_w_threes
        self.assertTrue(full_house_w_fours > full_house_w_threes)
    
if __name__ == "__main__":
    unittest.main()
    # player1_wins = 0
    # player2_wins = 0
    # with open("poker.txt") as f:
    #     for line in f.readlines():
    #         l = line.strip().split(" ")
    #         h1, h2 = Hand(l[0:5]), Hand(l[5:10])
    #         if h1 < h2:
    #             player2_wins += 1
    #         elif h2 < h1:
    #             player1_wins += 1
    # print player1_wins
