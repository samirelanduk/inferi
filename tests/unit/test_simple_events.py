from fractions import Fraction
from unittest import TestCase
from unittest.mock import Mock, patch
from inferi.probability import SimpleEvent, Event, SampleSpace

class SimpleEventTest(TestCase):

    def setUp(self):
        self.space = Mock(SampleSpace)



class SimpleEventCreationTests(SimpleEventTest):

    def test_can_create_simple_event(self):
        e = SimpleEvent("H", Fraction(1, 2), self.space)
        self.assertIsInstance(e, Event)
        self.assertEqual(e._outcome, "H")
        self.assertEqual(e._name, "H")
        self.assertEqual(e._probability, Fraction(1, 2))
        self.assertEqual(e._sample_space, self.space)
        self.assertEqual(e._simple_events, set([e]))


    def test_probability_must_be_numeric(self):
        with self.assertRaises(TypeError):
            SimpleEvent("H", "jj", self.space)


    def test_probability_must_be_valid(self):
        with self.assertRaises(ValueError):
            SimpleEvent("H", -0.1, self.space)
        with self.assertRaises(ValueError):
            SimpleEvent("H", 1.1, self.space)



class SimpleEventReprTests(SimpleEventTest):

    def test_simple_event_repr(self):
        e = SimpleEvent("H", 0.5, self.space)
        self.assertEqual(str(e), "<SimpleEvent: H>")



class SimpleEventOutcomeTests(SimpleEventTest):

    def test_simple_event_outcome(self):
        e = SimpleEvent("H", 0.5, self.space)
        self.assertEqual(e.outcome, e._outcome)
