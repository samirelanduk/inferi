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


    def test_events(self):
        # Rolling a die
        sample_space = inferi.SampleSpace(1, 2, 3, 4, 5, 6)
        self.assertEqual(len(sample_space.simple_events()), 6)
        self.assertEqual(sample_space.outcomes(), set(range(1, 7)))
