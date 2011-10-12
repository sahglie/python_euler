#!/opt/local/bin/python

import unittest
from s1 import Hand


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
        self.assertTrue(Hand(["AC", "2H", "3S", "4C", "5C"]).straight())
        self.assertFalse(Hand(["3C", "JH", "QS", "KC", "AC"]).straight())

    def test_one_pair(self):
        self.assertTrue(Hand(["2C", "2S", "4D", "5C", "6C"]).one_pair())
        self.assertFalse(Hand(["10C", "JH", "QS", "KC", "AC"]).one_pair())    

    def test_two_pair(self):
        self.assertTrue(Hand(["2C", "2S", "2D", "2H", "6C"]).two_pairs())
        self.assertFalse(Hand(["10C", "JH", "QS", "KC", "AC"]).two_pairs())   


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

    def test_confirm_hands(self):
        self.assertTrue(self.royal_flush.royal_flush())
        self.assertTrue(self.straight_flush.straight_flush())
        self.assertTrue(self.four_of_a_kind.four_of_a_kind())
        self.assertTrue(self.full_house.full_house())
        self.assertTrue(self.flush.flush())
        self.assertTrue(self.straight.straight())
        self.assertTrue(self.three_of_a_kind.three_of_a_kind())
        self.assertTrue(self.two_pairs.two_pairs())
        self.assertTrue(self.one_pair.one_pair())

    def test_highest_scoring_hand_always_wins(self):
        self.assertGreater(self.royal_flush, self.straight_flush)
        self.assertGreater(self.straight_flush, self.four_of_a_kind)
        self.assertGreater(self.four_of_a_kind, self.full_house)
        self.assertGreater(self.full_house, self.flush)
        self.assertGreater(self.flush, self.straight)
        self.assertGreater(self.straight, self.three_of_a_kind)
        self.assertGreater(self.three_of_a_kind, self.two_pairs)
        self.assertGreater(self.two_pairs, self.one_pair)


class TestBestHandWins(unittest.TestCase):
    def test_pair_of_fives_beats_pair_of_eights(self):
        pair_of_fives = Hand(["5H", "5C", "6S", "7S", "KD"])
        pair_of_eights = Hand(["2C", "3S", "8S", "8D", "TD"])
        self.assertGreater(pair_of_eights, pair_of_fives)

    def test_high_card_ace_beats_high_card_queen(self):
        highest_card_ace = Hand(["5D", "8C", "9S", "JS", "AC"])
        highest_card_queen = Hand(["2C", "5C", "7D", "8S", "QH"])
        self.assertGreater(highest_card_ace, highest_card_queen)

    def test_flush_w_diamonds_beats_three_aces(self):
        three_aces = Hand(["2D", "9C", "AS", "AH", "AC"])
        flush_w_diamonds = Hand(["3D", "6D", "7D", "TD", "QD"])
        self.assertGreater(flush_w_diamonds, three_aces)

    def test_two_queens_high_card_nine_beats_two_queens_high_card_seven(self):
        pair_of_queens_high_card_nine = Hand(["4D", "6S", "9H", "QH", "QC"])
        pair_of_queens_high_card_seven = Hand(["3D", "6D", "7H", "QD", "QS"])
        self.assertGreater(pair_of_queens_high_card_nine,
                           pair_of_queens_high_card_seven)

    def test_full_house_w_highest_three_of_a_kind_wins(self):
        full_house_w_fours = Hand(["2H", "2D", "4C", "4D", "4S"])
        full_house_w_threes = Hand(["3C", "3D", "3S", "9S", "9D"])
        self.assertGreater(full_house_w_fours, full_house_w_threes)

    def test_full_house_w_highest_pair_wind(self):
        full_house_w_twos = Hand(["2H", "2D", "4C", "4D", "4S"])
        full_house_w_threes = Hand(["3C", "3D", "4S", "4S", "4D"])
        self.assertGreater(full_house_w_threes, full_house_w_twos)

    def test_tied_two_pairs_w_highest_2nd_pair_wins(self):
        two_pairs_w_twos = Hand(["2H", "2D", "4C", "4D", "8S"])
        two_pairs_w_threes = Hand(["3C", "3D", "4S", "4S", "5D"])
        self.assertGreater(two_pairs_w_threes, two_pairs_w_twos)

    def test_highest_card_w_tied_two_pairs_wins(self):
        two_pairs_w_hight_card_five = Hand(["3H", "3D", "4C", "4D", "5S"])
        two_pairs_w_high_card_two = Hand(["3C", "3D", "4S", "4S", "2D"])
        self.assertGreater(two_pairs_w_hight_card_five,
                           two_pairs_w_high_card_two)

    def test_highest_card_w_tied_four_of_a_kind_wins(self):
        four_of_a_kind_w_high_card_eight = Hand(["2H", "2D", "2S", "2C", "8S"])
        four_of_a_kind_w_high_card_three = Hand(["2H", "2D", "2S", "2C", "3S"])
        self.assertGreater(four_of_a_kind_w_high_card_eight,
                           four_of_a_kind_w_high_card_three)

    def test_four_of_a_kind_w_highest_rank_wins(self):
        four_of_a_kind_w_aces = Hand(["AH", "AD", "AS", "AC", "8S"])
        four_of_a_kind_w_kings = Hand(["KH", "KD", "KS", "KC", "3S"])
        self.assertGreater(four_of_a_kind_w_aces, four_of_a_kind_w_kings)

    def test_highest_card_w_tied_flush_wins(self):
        flush_high_card_king = Hand(["3H", "4H", "5H", "9H", "KH"])
        flush_high_card_queen = Hand(["2D", "JD", "5D", "7D", "QD"])
        self.assertGreater(flush_high_card_king, flush_high_card_queen)


if __name__ == "__main__":
    unittest.main()
