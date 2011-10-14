#!/opt/local/bin/python

from collections import OrderedDict
import copy
from itertools import groupby
from operator import itemgetter


class Card:
    CARDS = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "T":10, "J":11, "Q":12, "K":13, "A":14}
    SUITS = set(["C", "D", "H", "S"])
    
    def __init__(self, card):
        self.card = card

    def suit(self):
        return self.card[-1:]

    def rank(self):
        return self.card[:-1]

    def value(self):
        return self.CARDS[self.rank()]

    def __cmp__(self, other):
        return self.value().__cmp__(other.value())
        

class CardGroup(OrderedDict):
    def __init__(self, groups):
        super(CardGroup, self).__init__(sorted(groups, key=itemgetter(1, 0)))

    def __cmp__(self, other):
        for v1, v2 in zip(self.keys(), other.keys())[::-1]:
            result = v1.__cmp__(v2)
            if result:
                return result
        return 0


class Hand:
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
        self.cards = [Card(c) for c in cards]
        self.cards.sort()
        groups = []
        for k, g in groupby(self.cards, lambda x: x.value()):
            groups.append((k, len(list(g))))
        self.card_groups = CardGroup(groups)

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

    A_ROYAL_FLUSH = [Card.CARDS["T"], Card.CARDS["J"], Card.CARDS["Q"], Card.CARDS["K"], Card.CARDS["A"]]
    
    def royal_flush(self):
        return self.flush() and [c.value() for c in self.cards] == self.A_ROYAL_FLUSH

    def straight_flush(self):
        return self.straight() and self.flush()

    def four_of_a_kind(self):
        return 4 in self.groups().values()

    def full_house(self):
        return 2 in self.groups().values() and \
               3 in self.groups().values()
    
    def flush(self):
        for suit in Card.SUITS:
            if map(lambda c: c.suit(), self.cards).count(suit) == 5:
                return True
        return False
    
    def straight(self):
        values = [c.value() for c in self.cards]
        if not self.__are_consecutive(values) and \
               Card.CARDS["2"] == values[0] and Card.CARDS["A"] == values[4]:
            values.pop(4)
        return self.__are_consecutive(values)

    def three_of_a_kind(self):
        return 3 in self.groups().values()

    def two_pairs(self):
        return self.groups().values().count(2) == 2
    
    def one_pair(self):
        return self.groups().values().count(2) == 1

    def groups(self):
        return copy.copy(self.card_groups)
    
    def __are_consecutive(self, values):
        for i in xrange(0, len(values)-1):
            if values[i]+1 != values[i+1]:
                return False
        return True
    
    def __cmp__(self, other):
        return self.score().__cmp__(other.score()) or \
               self.groups().__cmp__(other.groups()) or \
               max(self.groups().keys()).__cmp__(max(other.groups().keys()))

    
if __name__ == "__main__":
    p1_hands_won = 0
    with open("poker.txt") as f:
        for line in f.readlines():
            cards = line.strip().split(" ")
            p1_hand, p2_hand = Hand(cards[0:5]), Hand(cards[5:10])
            if p1_hand > p2_hand:
                p1_hands_won += 1
    print p1_hands_won
