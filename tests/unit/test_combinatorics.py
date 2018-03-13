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



class CombinationTests(TestCase):

    def test_can_get_combinations_of_1(self):
        self.assertEqual(combinations(1), 1)
        self.assertEqual(combinations(2), 1)
        self.assertEqual(combinations(4), 1)


    def test_can_get_useful_combinations(self):
        self.assertEqual(combinations(5, 3), 10)
        self.assertEqual(combinations(16, 9), 11440)


    def test_arguments_must_be_integers(self):
        with self.assertRaises(TypeError):
            combinations(5.5)
        with self.assertRaises(TypeError):
            combinations(7, 5.5)


    def test_r_must_be_less_than_n(self):
        with self.assertRaises(ValueError) as e:
            combinations(5, 6)
        self.assertIn("is larger than", str(e.exception))



class PermutatingTests(TestCase):

    def test_can_permutate_collection(self):
        self.assertEqual(set(permutate([1, 2])), set(((1, 2), (2, 1))))


    def test_can_sub_permutate_collection(self):
        self.assertEqual(set(permutate([1, 2, 3], 2)), set((
         (1, 2), (2, 1), (1, 3), (3, 1), (2, 3), (3, 2)
        )))


    def test_r_must_not_be_larger_than_n(self):
        with self.assertRaises(ValueError):
            permutate([1, 2, 3], 4)



class CombiningTests(TestCase):

    def test_can_combine_collection(self):
        self.assertEqual(list(combine([1, 2])), list([set([1, 2])]))


    def test_can_sub_combine_collection(self):
        combinations = list(combine([1, 2, 3], 2))
        self.assertEqual(len(combinations), 3)
        self.assertIn(set([1, 2]), combinations)
        self.assertIn(set([1, 3]), combinations)
        self.assertIn(set([3, 2]), combinations)


    def test_r_must_not_be_larger_than_n(self):
        with self.assertRaises(ValueError):
            list(combine([1, 2, 3], 4))