from unittest import TestCase
import inferi

class Tests(TestCase):

    def test_combinatorics(self):
        # How many ways of arranging six objects are there?
        self.assertEqual(inferi.permutations(6), 720)

        # How many ways of arranging three of five objects are there?
        self.assertEqual(inferi.permutations(6, 3), 120)
