from unittest import TestCase
from unittest.mock import Mock, patch
from inferi.probability import Event, SimpleEvent

class EventTest(TestCase):

    def setUp(self):
        self.simple_events = [Mock(SimpleEvent) for _ in range(10)]
        self.events = [Mock(Event), Mock(Event), Mock(Event)]
        for i, event in enumerate(self.simple_events, start=1):
            event._simple_events = set([event])
            event._probability = 5
            event._outcome = i
        for i, event in enumerate(self.events):
            event._simple_events = set(self.simple_events[i * 3: (i + 1) * 3])



class EventCreationTests(EventTest):

    def test_can_create_event_with_simple_events(self):
        event = Event(*self.simple_events)
        self.assertEqual(event._simple_events, set(self.simple_events))
        self.assertEqual(event._name, "E")


    def test_can_create_event_with_events(self):
        event = Event(*self.events)
        self.assertEqual(event._simple_events, set(self.simple_events[:-1]))
        self.assertEqual(event._name, "E")


    def test_can_create_event_with_name(self):
        event = Event(*self.simple_events, name="strike")
        self.assertEqual(event._name, "strike")


    def test_simple_events_must_be_simple_events(self):
        with self.assertRaises(TypeError):
            Event(self.simple_events[0], "event")


    def test_name_must_be_str(self):
        with self.assertRaises(TypeError):
            Event(self.simple_events[0], name=2)



class EventReprTests(EventTest):

    def test_event_repr(self):
        event = Event(*self.simple_events, name="strike")
        self.assertEqual(str(event), "<Event: strike>")



class EvenntContainerTests(EventTest):

    def test_outcomes_in_event(self):
        event = Event(*self.simple_events)
        for n in range(1, 10): self.assertIn(n, event)
        self.assertNotIn(20, event)


    def test_simple_events_in_event(self):
        event = Event(*self.simple_events[:5])
        for e in self.simple_events[:5]: self.assertIn(e, event)
        for e in self.simple_events[5:]: self.assertNotIn(e, event)


    def test_events_in_event(self):
        event = Event(*self.simple_events[3:7])
        mock_event = Mock(Event)
        mock_event._simple_events = set(self.simple_events[4:6])
        self.assertIn(mock_event, event)
        mock_event._simple_events = set(self.simple_events[4:8])
        self.assertNotIn(mock_event, event)



class EventSimpleEvents(EventTest):

    def test_can_get_event_simple_events(self):
        event = Event(*self.simple_events)
        self.assertEqual(event.simple_events(), event._simple_events)
        self.assertIsNot(event.simple_events(), event._simple_events)



class EventNameTests(EventTest):

    def test_can_get_event_name(self):
        event = Event(*self.simple_events, name="strike")
        self.assertEqual(event._name, event.name())



class EventProbabilityTests(EventTest):

    def test_can_get_event_probability(self):
        event = Event(*self.simple_events)
        self.assertEqual(event.probability(), 50)



class EventMutualExclusivityTests(EventTest):

    def test_not_mutually_exclusive_if_simple_events_in_common(self):
        event = Event(*self.simple_events[:5])
        mock_event = Mock(Event)
        mock_event._simple_events = set(self.simple_events[4:])
        self.assertFalse(event.mutually_exclusive_with(mock_event))


    def test_mutually_exclusive_if_no_simple_events_in_common(self):
        event = Event(*self.simple_events[:5])
        mock_event = Mock(Event)
        mock_event._simple_events = set(self.simple_events[5:])
        self.assertTrue(event.mutually_exclusive_with(mock_event))


    def test_mutually_exclusive_needs_event(self):
        event = Event(*self.simple_events)
        with self.assertRaises(TypeError):
            event.mutually_exclusive_with("e")
