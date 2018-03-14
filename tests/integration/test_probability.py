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

        # These permutations and combinations can actually be produced
        options = ["A", "B", "C", "D", "E"]
        self.assertEqual(set(inferi.permutate(options, 2)), set((
         ("A", "B"), ("B", "A"), ("A", "C"), ("C", "A"), ("A", "D"),
         ("D", "A"), ("A", "E"), ("E", "A"), ("B", "C"), ("C", "B"),
         ("B", "D"), ("D", "B"), ("B", "E"), ("E", "B"), ("C", "D"),
         ("D", "C"), ("C", "E"), ("E", "C"), ("D", "E"), ("E", "D")
        )))
        combinations = tuple(inferi.combine(options, 2))
        self.assertEqual(len(combinations), 10)
        for set_ in (
         set(["A", "B"]), set(["A", "C"]), set(["A", "D"]), set(["A", "E"]),
         set(["B", "C"]), set(["B", "D"]), set(["B", "E"]), set(["C", "D"]),
         set(["C", "E"]), set(["D", "E"])
        ):
            self.assertIn(set_, combinations)


    def test_events(self):
        # Rolling a die
        sample_space = inferi.SampleSpace(1, 2, 3, 4, 5, 6)
        self.assertEqual(len(sample_space.simple_events()), 6)
        self.assertEqual(sample_space.outcomes(), set(range(1, 7)))
        self.assertIn(4, sample_space)
        self.assertNotIn(4.5, sample_space)
        for event in sample_space.simple_events():
            self.assertEqual(event.probability(), 1 / 6)
        self.assertEqual(sample_space.chances_of(0), 0)
        self.assertEqual(sample_space.chances_of(1), 1 / 6)
        self.assertEqual(sample_space.chances_of(6), 1 / 6)
        self.assertEqual(sample_space.chances_of(7), 0)
        self.assertIn(sample_space.event(2), sample_space.simple_events())
        self.assertEqual(sample_space.event(5).outcome(), 5)
        for i in range(1000):
            self.assertIn(sample_space.experiment(), range(1, 7))

        # Unfair die

        # Rolling six die

        # Picking cards
