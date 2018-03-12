from unittest import TestCase
import inferi

class Tests(TestCase):

    def test_combinatorics(self):
        # How many ways of arranging six objects are there?
        self.assertEqual(inferi.permutations(6), 720)

        # How many ways of arranging three of five objects are there?
        self.assertEqual(inferi.permutations(6, 3), 120)

        # How many combinations of six objects are there?
        self.assertEqual(inferi.combinations(6), 1)
        self.assertEqual(inferi.combinations(6, 5), 6)
        self.assertEqual(inferi.combinations(6, 4), 15)
        self.assertEqual(inferi.combinations(6, 3), 20)
        self.assertEqual(inferi.combinations(6, 2), 15)
