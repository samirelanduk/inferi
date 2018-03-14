from unittest import TestCase
from unittest.mock import Mock, patch
from inferi.probability import Event, SimpleEvent

class EventTest(TestCase):

    def setUp(self):
        self.simple_events = [Mock(SimpleEvent), Mock(SimpleEvent), Mock(SimpleEvent)]
        self.simple_events[0].outcome.return_value = "H"
        self.simple_events[1].outcome.return_value = "T"
        self.simple_events[2].outcome.return_value = "S"
        self.simple_events[0].probability.return_value = 0.33
        self.simple_events[1].probability.return_value = 0.33
        self.simple_events[2].probability.return_value = 0.33



class EventCreationTests(EventTest):

    def test_can_create_event(self):
        event = Event(*self.simple_events)
        self.assertEqual(event._simple_events, set(self.simple_events))
        self.assertEqual(event._name, "E")


    def test_can_create_event_with_name(self):
        event = Event(*self.simple_events, name="strike")
        self.assertEqual(event._simple_events, set(self.simple_events))
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
        self.assertEqual(str(event), "<Event 'strike'>")



class EventSimpleEvents(EventTest):

    def test_can_get_event_simple_events(self):
        event = Event(*self.simple_events, name="strike")
        self.assertEqual(event.simple_events(), event._simple_events)
        self.assertIsNot(event.simple_events(), event._simple_events)



class EventNameTests(EventTest):

    def test_can_get_event_name(self):
        event = Event(*self.simple_events, name="strike")
        self.assertEqual(event._name, event.name())



class EventProbabilityTests(EventTest):

    def test_can_get_event_probability(self):
        event = Event(*self.simple_events)
        self.assertEqual(event.probability(), 0.99)
        for e in self.simple_events:
            e.probability.assert_called_with()



class EventMutualExclusivityTests(EventTest):

    def test_event_mutually_exclusive_with_simple_event(self):
        event = Event(*self.simple_events)
        self.assertFalse(event.mutually_exclusive_with(self.simple_events[0]))
        event = Event(*self.simple_events[1:])
        self.assertTrue(event.mutually_exclusive_with(self.simple_events[0]))


    def test_event_mutually_exclusive_with_event(self):
        event = Event(*self.simple_events[:2])
        mock_event = Mock(Event)
        mock_event._simple_events = set(self.simple_events[1:])
        self.assertFalse(event.mutually_exclusive_with(mock_event))
        mock_event._simple_events = set(self.simple_events[2:])
        self.assertTrue(event.mutually_exclusive_with(mock_event))


    def test_mutually_exclusive_needs_event(self):
        event = Event(*self.simple_events)
        with self.assertRaises(TypeError):
            event.mutually_exclusive_with("e")
