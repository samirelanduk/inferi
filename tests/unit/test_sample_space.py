from fractions import Fraction
from unittest import TestCase
from unittest.mock import Mock, patch
from inferi.probability import SampleSpace, Event, EventSpace

class SampleSpaceTest(TestCase):

    def setUp(self):
        self.patch1 = patch("inferi.probability.SimpleEvent")
        self.mock_simple_event = self.patch1.start()
        self.simple_events = [Mock(), Mock(), Mock()]
        self.simple_events[0].outcome = "H"
        self.simple_events[1].outcome = "T"
        self.simple_events[2].outcome = "S"
        self.simple_events[0].probability.return_value = 0.33
        self.simple_events[1].probability.return_value = 0.33
        self.simple_events[2].probability.return_value = 0.33
        self.mock_simple_event.side_effect = self.simple_events


    def tearDown(self):
        self.patch1.stop()



class SampleSpaceCreationTests(SampleSpaceTest):

    def test_can_create_sample_space_from_outcomes(self):
        space = SampleSpace("H", "T")
        self.assertIsInstance(space, EventSpace)
        self.assertEqual(space._simple_events, set(self.simple_events[:2]))
        self.mock_simple_event.assert_any_call("H", Fraction(1, 2), space)
        self.mock_simple_event.assert_any_call("T", Fraction(1, 2), space)


    def test_sample_space_needs_outcomes(self):
        with self.assertRaises(ValueError):
            SampleSpace()


    def test_can_create_sample_space_with_probabilities(self):
        space = SampleSpace("H", "T", p={"H": 0.2, "T": 0.8})
        self.assertEqual(space._simple_events, set(self.simple_events[:2]))
        self.mock_simple_event.assert_any_call("H", Fraction(1, 5), space)
        self.mock_simple_event.assert_any_call("T", Fraction(4, 5), space)


    def test_can_create_sample_space_with_missing_probabilities(self):
        space = SampleSpace("H", "T", p={"H": 0.2})
        self.assertEqual(space._simple_events, set(self.simple_events[:2]))
        self.mock_simple_event.assert_any_call("H", Fraction(1, 5), space)
        self.mock_simple_event.assert_any_call("T", Fraction(4, 5), space)


    def test_can_create_sample_space_with_extra_probabilities(self):
        space = SampleSpace("H", "T", p={"H": 0.2, "S": 0.45})
        self.assertEqual(space._simple_events, set(self.simple_events))
        self.mock_simple_event.assert_any_call("H", Fraction(1, 5), space)
        self.mock_simple_event.assert_any_call("T", Fraction(7, 20), space)
        self.mock_simple_event.assert_any_call("S", Fraction(9, 20), space)


    def test_can_create_sample_space_with_only_probabilities(self):
        space = SampleSpace(p={"H": 0.2, "S": 0.8})
        self.assertEqual(space._simple_events, set(self.simple_events[:2]))
        self.mock_simple_event.assert_any_call("H", Fraction(1, 5), space)
        self.mock_simple_event.assert_any_call("S", Fraction(4, 5), space)


    def test_probabilities_cant_add_up_to_more_than_1(self):
        SampleSpace("T", p={"T": 1})
        with self.assertRaises(ValueError):
            SampleSpace(p={"T": 1.1})


    def test_probabilities_cant_add_up_to_less_than_1(self):
        with self.assertRaises(ValueError):
            SampleSpace("H", "T", p={"H": 0.3, "T": 0.4})



class SampleSpaceReprTests(SampleSpaceTest):

    def test_sample_space_repr(self):
        space = SampleSpace("H", "T")
        self.assertEqual(str(space), "<SampleSpace (2 simple events)>")



class SampleSpaceEventTests(SampleSpaceTest):

    def test_can_get_simple_event(self):
        space = SampleSpace("H", "T", "S")
        self.assertIs(space.event("H"), self.simple_events[0])
        self.assertIs(space.event("S"), self.simple_events[2])


    def test_can_return_no_simple_event(self):
        space = SampleSpace("H", "T", "S")
        self.assertIsNone(space.event("A"))


    @patch("inferi.probability.Event")
    def test_can_get_event_from_multiple_outcomes(self, mock_event):
        mock_event.return_value = "EVENT"
        space = SampleSpace("H", "T", "S")
        e = space.event("H", "T")
        args, kwargs = mock_event.call_args_list[0]
        self.assertEqual(set(args), set(self.simple_events[:2]))
        self.assertEqual(kwargs, {})
        self.assertEqual(e, "EVENT")


    @patch("inferi.probability.Event")
    def test_can_get_event_with_name(self, mock_event):
        mock_event.return_value = "EVENT"
        space = SampleSpace("H", "T", "S")
        e = space.event("H", "T", name="coin")
        args, kwargs = mock_event.call_args_list[0]
        self.assertEqual(set(args), set(self.simple_events[:2]))
        self.assertEqual(kwargs, {"name": "coin"})
        self.assertEqual(e, "EVENT")


    @patch("inferi.probability.Event")
    def test_can_get_event_with_lambda(self, mock_event):
        mock_event.return_value = "EVENT"
        space = SampleSpace("H", "T", "S")
        e = space.event(lambda o: o in ("T", "S"))
        args, kwargs = mock_event.call_args_list[0]
        self.assertEqual(set(args), set(self.simple_events[1:]))
        self.assertEqual(kwargs, {})
        self.assertEqual(e, "EVENT")



class SampleSpaceChancesOfTests(SampleSpaceTest):

    @patch("inferi.probability.SampleSpace.event")
    def test_can_get_chances_of(self, mock_event):
        mock_event.return_value = self.simple_events[0]
        space = SampleSpace("H", "T")
        self.assertEqual(space.chances_of("H", 5), 0.33)
        mock_event.assert_called_with("H", 5)
        self.simple_events[0].probability.assert_called_with()


    @patch("inferi.probability.SampleSpace.event")
    def test_can_get_chances_of_no_event(self, mock_event):
        mock_event.return_value = None
        space = SampleSpace("H", "T")
        f = lambda a: a
        self.assertEqual(space.chances_of(f), 0)
        mock_event.assert_called_with(f)



class SampleSpaceExperimentTests(SampleSpaceTest):

    def setUp(self):
        SampleSpaceTest.setUp(self)
        self.patch2 = patch("inferi.probability.SampleSpace.outcomes")
        self.mock_outcomes = self.patch2.start()
        self.mock_outcomes.return_value = {"H": 0.33, "T": 0.33}


    def tearDown(self):
        self.patch2.stop()
        SampleSpaceTest.tearDown(self)


    def test_can_run_statistical_experiment(self):
        space = SampleSpace("H", "T")
        results = [space.experiment() for _ in range(100)]
        self.assertEqual(set(results), set(["H", "T"]))
        self.assertGreaterEqual(results.count("H"), 35)
        self.assertGreaterEqual(results.count("T"), 35)
        self.mock_outcomes.assert_called_with(p=True)
