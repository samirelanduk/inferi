from unittest import TestCase
from unittest.mock import Mock, patch
from inferi.probability import SampleSpace, Event, EventSpace, SimpleEvent

class EventSpaceTest(TestCase):

    def setUp(self):
        self.simple_events = [Mock(SimpleEvent) for _ in range(3)]
        self.simple_events[0].outcome.return_value = "H"
        self.simple_events[1].outcome.return_value = "T"
        self.simple_events[2].outcome.return_value = "S"
        for e in self.simple_events:
            e.probability.return_value = 0.33
            e.simple_events.return_value = {e}
        self.space = EventSpace()
        self.space._simple_events = set(self.simple_events)



class EventSpaceContainerTests(EventSpaceTest):

    def test_can_look_for_simple_events(self):
        self.space._simple_events = set(self.simple_events[:-1])
        self.assertIn(self.simple_events[0], self.space)
        self.assertIn(self.simple_events[1], self.space)
        self.assertNotIn(self.simple_events[2], self.space)


    def test_can_look_for_events(self):
        self.space._simple_events = set(self.simple_events[:-1])
        event = Mock(Event)
        event.simple_events.return_value = set(self.simple_events[:2])
        self.assertIn(event, self.space)


    def test_can_look_for_outcomes(self):
        self.space._simple_events = set(self.simple_events[:-1])
        self.assertIn("H", self.space)
        self.assertIn("T", self.space)
        self.assertNotIn("S", self.space)



class EventSpaceSimpleEventsTests(EventSpaceTest):

    def test_sample_space_simple_events(self):
        self.assertEqual(self.space.simple_events(), self.space._simple_events)
        self.assertIsNot(self.space.simple_events(), self.space._simple_events)



class EventSpaceOutcomesTests(EventSpaceTest):

    def test_can_get_outcomes(self):
        outcomes = self.space.outcomes()
        for event in self.simple_events: event.outcome.assert_called_with()
        self.assertEqual(outcomes, set(["H", "T", "S"]))


    def test_can_get_outcomes_with_odds(self):
        outcomes = self.space.outcomes(p=True)
        for event in self.simple_events: event.outcome.assert_called_with()
        self.assertEqual(outcomes, {"H": 0.33, "T": 0.33, "S": 0.33})
