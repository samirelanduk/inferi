from unittest import TestCase
from unittest.mock import Mock, patch
from inferi.probability import SimpleEvent

class SimpleEventCreationTests(TestCase):

    def test_can_create_simple_event(self):
        e = SimpleEvent("H")
        self.assertEqual(e._outcome, "H")



class SimpleEventReprTests(TestCase):

    def test_simple_event_repr(self):
        e = SimpleEvent("H")
        self.assertEqual(str(e), "<SimpleEvent: H>")



class SimpleEventOutcomeTests(TestCase):

    def test_simple_event_outcome(self):
        e = SimpleEvent("H")
        self.assertEqual(e.outcome(), e._outcome)
