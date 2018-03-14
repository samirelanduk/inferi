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

        # How many outcomes are there of a three-stage experiment?
        self.assertEqual(inferi.multiplications(6), 6)
        self.assertEqual(inferi.multiplications(6, 3), 18)
        self.assertEqual(inferi.multiplications(6, 6, 3), 108)

        # These permutations and combinations etc. can actually be produced
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
        self.assertEqual(tuple(inferi.multiply(options, options)), (
         ("A", "A"), ("A", "B"), ("A", "C"), ("A", "D"), ("A", "E"),
         ("B", "A"), ("B", "B"), ("B", "C"), ("B", "D"), ("B", "E"),
         ("C", "A"), ("C", "B"), ("C", "C"), ("C", "D"), ("C", "E"),
         ("D", "A"), ("D", "B"), ("D", "C"), ("D", "D"), ("D", "E"),
         ("E", "A"), ("E", "B"), ("E", "C"), ("E", "D"), ("E", "E")
        ))


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
        event = sample_space.event(2, 5, name="2 or 5")
        self.assertEqual(event.name(), "2 or 5")
        self.assertEqual(event.probability(), 1 / 3)
        event = sample_space.event(lambda o: o % 2 == 0, name="even")
        self.assertEqual(event.probability(), 1 / 2)
        self.assertEqual(len(event.simple_events()), 3)

        # Unfair die
        sample_space = inferi.SampleSpace(1, 2, 3, 4, 5, 6, p={4: 0.3})
        self.assertEqual(len(sample_space.simple_events()), 6)
        self.assertEqual(sample_space.chances_of(6), 0.7 / 5)
        self.assertEqual(sample_space.chances_of(5), 0.7 / 5)
        self.assertEqual(sample_space.chances_of(4), 0.3)
        outcomes = [sample_space.experiment() for _ in range(1000)]
        self.assertGreaterEqual(outcomes.count(4), 200)
        event = sample_space.event(lambda o: o % 2 == 0, name="even")
        self.assertEqual(event.probability(), 2.9 / 5)
        self.assertEqual(len(event.simple_events()), 3)

        # Rolling two die
        dice = [1, 2, 3, 4, 5, 6]
        sample_space = inferi.SampleSpace(*inferi.multiply(dice, dice))
        self.assertEqual(len(sample_space.simple_events()), 36)
        self.assertEqual(sample_space.chances_of((6, 6)), 1 / 36)
        event = sample_space.event(lambda o: sum(o) == 10, name="ten")
        self.assertEqual(event.probability(), 3 / 36)

        # Picking cards
        cards = inferi.multiply(["H", "D", "S", "C"], range(13))
        sample_space = inferi.SampleSpace(*cards)
        self.assertEqual(sample_space.chances_of(("S", 0)), 1 / 52)
