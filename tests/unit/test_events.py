from fractions import Fraction
from unittest import TestCase
from unittest.mock import Mock, patch
from inferi.probability import Event, SimpleEvent

class EventTest(TestCase):

    def setUp(self):
        self.simple_events = [Mock(SimpleEvent) for _ in range(10)]
        self.events = [Mock(Event), Mock(Event), Mock(Event)]
        for i, event in enumerate(self.simple_events, start=1):
            event._simple_events = set([event])
            event._probability = Fraction(5, 1)
            event._outcome = i
            event._sample_space = "SPACE"
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



class EventOrTests(EventTest):

    def test_can_get_event_or(self):
        event = Event(*self.simple_events[:3])
        mock_event = Mock(Event)
        mock_event._simple_events = set(self.simple_events[3:6])
        new = event | mock_event
        self.assertEqual(new._simple_events, set(self.simple_events[:6]))


    def test_or_needs_event(self):
        event = Event(*self.simple_events[:3])
        with self.assertRaises(TypeError):
            event | "event"



class EventAndTests(EventTest):

    def test_can_get_event_and(self):
        event = Event(*self.simple_events[:4])
        mock_event = Mock(Event)
        mock_event._simple_events = set(self.simple_events[3:6])
        new = event & mock_event
        self.assertEqual(new._simple_events, set(self.simple_events[3:4]))


    def test_can_get_empty_event_and(self):
        event = Event(*self.simple_events[:3])
        mock_event = Mock(Event)
        mock_event._simple_events = set(self.simple_events[3:6])
        new = event & mock_event
        self.assertEqual(new._simple_events, set())


    def test_and_needs_event(self):
        event = Event(*self.simple_events[:3])
        with self.assertRaises(TypeError):
            event | "event"



class EventComplementTests(EventTest):

    @patch("inferi.probability.Event.sample_space")
    def test_can_get_event_complement(self, mock_sample_space):
        space = Mock()
        mock_sample_space.return_value = space
        space.simple_events.return_value = set(self.simple_events)
        event = Event(*self.simple_events[:3])
        not_ = event.complement()
        self.assertEqual(not_._simple_events, set(self.simple_events[3:]))



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
        event = Event(*self.simple_events[:2])
        self.simple_events[0]._probability = Fraction(1, 6)
        self.simple_events[1]._probability = Fraction(1, 6)
        event._probability = Fraction(1, 6)
        self.assertEqual(event.probability(), 2 / 6)


    def test_can_get_event_probability_as_fraction(self):
        event = Event(*self.simple_events[:2])
        self.simple_events[0]._probability = Fraction(1, 6)
        self.simple_events[1]._probability = Fraction(1, 6)
        event._probability = Fraction(1, 6)
        self.assertEqual(event.probability(fraction=True), Fraction(1, 3))


    def test_can_get_probability_given_other_event(self):
        event = Event(*self.simple_events[:5])
        self.events[1].probability.return_value = 2
        self.assertEqual(event.probability(given=self.events[1]), 5)


    def test_given_event_must_be_event(self):
        event = Event(*self.simple_events[:5])
        with self.assertRaises(TypeError):
            event.probability(given="event")



class SimpleEventSampleSpaceTests(EventTest):

    def test_event_sample_space(self):
        event = Event(*self.simple_events)
        self.assertEqual(event.sample_space(), "SPACE")



class EventOutcomesTests(EventTest):

    def test_can_get_outcomes(self):
        event = Event(*self.simple_events)
        outcomes = event.outcomes()
        self.assertEqual(outcomes, set(range(1, 11)))


    def test_can_get_outcomes_with_odds(self):
        event = Event(*self.simple_events)
        outcomes = event.outcomes(p=True)
        self.assertEqual(outcomes, {i: 5 for i in range(1, 11)})



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



class EventIndependenceTests(EventTest):

    @patch("inferi.probability.Event.probability")
    def test_independence(self, mock_p):
        event = Event(*self.simple_events)
        mock_event = Mock(Event)
        mock_p.return_value = 0.5, 0.5
        self.assertTrue(event.independent_of(mock_event))
        mock_p.assert_any_call(fraction=True)
        mock_p.assert_any_call(fraction=True, given=mock_event)
        mock_p.side_effect = (0.5, 0.6)
        self.assertFalse(event.independent_of(mock_event))


    def test_independence_needs_event(self):
        event = Event(*self.simple_events)
        with self.assertRaises(TypeError):
            event.independent_of("e")



class EventDependenceTests(EventTest):

    @patch("inferi.probability.Event.independent_of")
    def test_dependence(self, mock_ind):
        event = Event(*self.simple_events)
        mock_event = Mock(Event)
        mock_ind.return_value = False
        self.assertTrue(event.dependent_on(mock_event))
        mock_ind.assert_called_with(mock_event)
        mock_ind.return_value = True
        self.assertFalse(event.dependent_on(mock_event))
