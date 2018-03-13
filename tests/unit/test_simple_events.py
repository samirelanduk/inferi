from unittest import TestCase
from unittest.mock import Mock, patch
from inferi.probability import SimpleEvent

class SimpleEventCreationTests(TestCase):

    def test_can_create_simple_event(self):
        e = SimpleEvent("H", 0.5)
        self.assertEqual(e._outcome, "H")
        self.assertEqual(e._probability, 0.5)


    def test_probability_must_be_numeric(self):
        with self.assertRaises(TypeError):
            SimpleEvent("H", "jj")


    def test_probability_must_be_valid(self):
        with self.assertRaises(ValueError):
            SimpleEvent("H", -0.1)
        with self.assertRaises(ValueError):
            SimpleEvent("H", 1.1)



class SimpleEventReprTests(TestCase):

    def test_simple_event_repr(self):
        e = SimpleEvent("H", 0.5)
        self.assertEqual(str(e), "<SimpleEvent: H>")



class SimpleEventOutcomeTests(TestCase):

    def test_simple_event_outcome(self):
        e = SimpleEvent("H", 0.5)
        self.assertEqual(e.outcome(), e._outcome)



class SimpleEventProbabilityTests(TestCase):

    def test_simple_event_probability(self):
        e = SimpleEvent("H", 0.5)
        self.assertEqual(e.probability(), e._probability)
