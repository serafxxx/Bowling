import unittest

from bowling import count_bowling_score, BowlingException


class TestBowlingScoreCounter(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(count_bowling_score([9, 0, 3, 5, 6, 1, 3, 6, 8, 1, 5, 3, 2, 5, 8, 0, 7, 1, 8, 1]), 82)

    def test_spare(self):
        self.assertEqual(count_bowling_score([9, 0, 3, 7, 6, 1, 3, 7, 8, 1, 5, 5, 0, 10, 8, 0, 7, 3, 8, 2, 8]), 131)

    def test_strike(self):
        self.assertEqual(count_bowling_score([10, 3, 7, 6, 1, 10, 10, 10, 2, 8, 9, 0, 7, 3, 10, 10, 10]), 193)

    def test_ignore_redundant(self):
        self.assertEqual(count_bowling_score([10, 3, 7, 6, 1, 10, 10, 10, 2, 8, 9, 0, 7, 3, 10, 10, 10, 1, 20, 5]), 193)

    def test_game_in_progress(self):
        self.assertEqual(count_bowling_score([]), 0)
        self.assertEqual(count_bowling_score([10, ]), 10)
        self.assertEqual(count_bowling_score([10, 5, 5]), 30)

    def test_wrong_data(self):
        self.assertRaises(BowlingException, count_bowling_score, [20, 30, 40])
        self.assertRaises(BowlingException, count_bowling_score, [-1, -2, -3])
        self.assertRaises(BowlingException, count_bowling_score, [None, ])
        self.assertRaises(BowlingException, count_bowling_score, ['WTF', ])
        self.assertRaises(BowlingException, count_bowling_score, 'WTF')

    def test_wrong_frame_score(self):
        # You can't bowl more than 10 pins per frame
        self.assertRaises(BowlingException, count_bowling_score, [9, 2, ])
        self.assertRaises(BowlingException, count_bowling_score, [10, 2, 9])

    def test_max_game_score(self):
        looong_list_of_strikes = [10 for i in xrange(100)]
        self.assertEqual(count_bowling_score(looong_list_of_strikes), 300)


if __name__ == '__main__':
    unittest.main()
