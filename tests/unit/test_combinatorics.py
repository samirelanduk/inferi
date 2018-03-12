from unittest import TestCase
from unittest.mock import Mock, patch
from inferi.combinatorics import *

class PermutationTests(TestCase):

    def test_can_get_simple_permutations(self):
        self.assertEqual(permutations(1), 1)
        self.assertEqual(permutations(2), 2)
        self.assertEqual(permutations(4), 24)


    def test_can_get_sub_permutations(self):
        self.assertEqual(permutations(5, 3), 60)


    def test_arguments_must_be_integers(self):
        with self.assertRaises(TypeError):
            permutations(5.5)
        with self.assertRaises(TypeError):
            permutations(7, 5.5)


    def test_r_must_be_less_than_n(self):
        with self.assertRaises(ValueError) as e:
            permutations(5, 6)
        self.assertIn("is larger than", str(e.exception))
