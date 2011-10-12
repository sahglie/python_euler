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

How many hands does Player 1 win?
"""


class Hand:
    CARDS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14"]
    SUITS = set(["C", "D", "H", "S"])
    HIGH_CARD_MAPPING = {"T":"10", "J":"11", "Q":"12", "K":"13", "A":"14"}

    ROYAL_FLUSH     = 9
    STRAIGHT_FLUSH  = 8
    FOUR_OF_A_KIND  = 7
    FULL_HOUSE      = 6
    FLUSH           = 5
    STRAIGHT        = 4
    THREE_OF_A_KIND = 3
    TWO_PAIRS       = 2
    ONE_PAIR        = 1
    NO_HAND         = 0

    def __init__(self, cards):
        self.str_cards = cards[::]
        for m in self.HIGH_CARD_MAPPING:
            for i, card in enumerate(cards):
                if card.startswith(m):
                    cards[i] = card.replace(m, self.HIGH_CARD_MAPPING[m])
        cards.sort(key=self.rank_score)
        self.cards = tuple(cards)

    def __str__(self):
        return self.str_cards
    
    def score(self):
        if self.royal_flush():
            return self.ROYAL_FLUSH
        elif self.straight_flush():
            return self.STRAIGHT_FLUSH
        elif self.four_of_a_kind():
            return self.FOUR_OF_A_KIND
        elif self.full_house():
            return self.FULL_HOUSE
        elif self.flush():
            return self.FLUSH
        elif self.straight():
            return self.STRAIGHT
        elif self.three_of_a_kind():
            return self.THREE_OF_A_KIND
        elif self.two_pairs():
            return self.TWO_PAIRS
        elif self.one_pair():
            return self.ONE_PAIR
        else:
            return self.NO_HAND

    def royal_flush(self):
        """Royal Flush: Ten, Jack, Queen, King, Ace, in same suit."""
        return self.flush() and map(self.rank, self.cards) == self.CARDS[8:]

    def straight_flush(self):
        """Straight Flush: All cards are consecutive values of same suit."""
        return self.straight() and self.flush()

    def four_of_a_kind(self):
        """Four of a Kind: Four cards of the same value."""
        return self.__find_repeating_rank(4, self.cards) > -1

    def full_house(self):
        """Full House: Three of a kind and a pair."""
        return self.__has_pairs(3, 2)
    
    def flush(self):
        """Flush: All cards of the same suit."""
        for suit in self.SUITS:
            if all(map(lambda x: self.suit(x) == suit, self.cards)):
                return True
        return False
    
    def straight(self):
        """Straight: All cards are consecutive values."""
        values = map(self.rank_score, self.cards)
        if self.__are_consecutive(values):
            return True
        elif self.__is_ace(values[4]):
            values[4] = 1
            values.sort()
            return self.__are_consecutive(values)
        else:
            return False

    def three_of_a_kind(self):
        """Three of a Kind: Three cards of the same value."""
        return self.__find_repeating_rank(3, self.cards) > -1

    def two_pairs(self):
        """Two Pairs: Two different pairs."""
        return self.__has_pairs(2, 2)
    
    def one_pair(self):
        """One Pair: Two cards of the same value."""
        return self.__find_repeating_rank(2, self.cards) > -1

    def suit(self, card):
        return card[-1:]

    def rank(self, card):
        return card[:-1]

    def rank_score(self, card):
        return int(self.rank(card))

    def __nth_highest_card_score(self, n = 1):
        cards = map(int, list(set(map(self.rank, self.cards))))
        cards.sort()
        return cards[::-1][n-1]

    def __score_repeating_rank(self, n):
        index = self.__find_repeating_rank(n, self.cards)
        return self.rank_score(self.cards[index])

    def __is_ace(self, card):
        return card == 14
    
    def __find_repeating_rank(self, n, cards):
        values = map(self.rank, cards)
        for i, rank in enumerate(values):
            if values.count(rank) >= n:
                return i
        return -1

    def __has_pairs(self, pair1_count, pair2_count):
        cards = list(self.cards)
        index = self.__find_repeating_rank(pair1_count, cards)
        if index > -1:
            for i in range(index, index+pair1_count):
                cards.pop(index)
            return self.__find_repeating_rank(pair2_count, cards) > -1
        else:
            return False

    def __are_consecutive(self, values):
        equalized = [values[0], values[1]-1, values[2]-2, values[3]-3, values[4]-4]
        return equalized.count(values[0]) == 5
               
    def __cmp__(self, other_hand):
        if self.score() < other_hand.score():
            return -1
        elif self.score() > other_hand.score():
            return 1
        else:
            if self.score() == self.FULL_HOUSE:
                return self.__cmp_pairs(other_hand, [3, 2])
            elif self.score() == self.FOUR_OF_A_KIND:
                return self.__cmp_pairs(other_hand, [4])
            elif self.score() == self.THREE_OF_A_KIND:
                return self.__cmp_pairs(other_hand, [3])
            elif self.score() == self.TWO_PAIRS:
                return self.__cmp_pairs(other_hand, [2, 2])
            elif self.score() == self.ONE_PAIR:
                return self.__cmp_pairs(other_hand, [2])
            else:
                return self.__cmp_highest_card(other_hand)

    def __cmp_pairs(self, other_hand, pairs_length):
        for l in pairs_length:
            if self.__score_repeating_rank(l) < other_hand.__score_repeating_rank(l):
                return -1
            elif self.__score_repeating_rank(l) > other_hand.__score_repeating_rank(l):
                return 1
        return self.__cmp_highest_card(other_hand)
        
    def __cmp_highest_card(self, other):
        n = 1
        while True:
            if self.__nth_highest_card_score(n) < other.__nth_highest_card_score(n):
                return -1
            elif self.__nth_highest_card_score(n) > other.__nth_highest_card_score(n):
                return 1
            n += 1

    
if __name__ == "__main__":
    player1_wins = 0
    with open("poker.txt") as f:
        for line in f.readlines():
            cards = line.strip().split(" ")
            h1, h2 = Hand(cards[0:5]), Hand(cards[5:10])
            if h1 > h2:
                player1_wins += 1
    print player1_wins
