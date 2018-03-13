from unittest import TestCase
from unittest.mock import Mock, patch
from inferi.probability import SampleSpace

class SampleSpaceTest(TestCase):

    def setUp(self):
        self.patch1 = patch("inferi.probability.SimpleEvent")
        self.mock_simple_event = self.patch1.start()
        self.mock_simple_event.side_effect = lambda o, p: o


    def tearDown(self):
        self.patch1.stop()



class SampleSpaceCreationTests(SampleSpaceTest):

    def test_can_create_sample_space(self):
        space = SampleSpace("H", "T")
        self.assertEqual(space._simple_events, set(["H", "T"]))
        self.mock_simple_event.assert_any_call("H", 0.5)
        self.mock_simple_event.assert_any_call("T", 0.5)



class SampleSpaceReprTests(SampleSpaceTest):

    def test_sample_space_repr(self):
        space = SampleSpace("H", "T")
        self.assertEqual(str(space), "<SampleSpace (2 simple events)>")



class SampleSpaceSimpleEvents(SampleSpaceTest):

    def test_sample_space_simple_events(self):
        space = SampleSpace("H", "T")
        self.assertEqual(space.simple_events(), space._simple_events)
        self.assertIsNot(space.simple_events(), space._simple_events)



class SampleSpaceOutcomesTests(SampleSpaceTest):

    def test_can_get_outcomes(self):
        events = [Mock(), Mock(), Mock()]
        events[0].outcome.return_value = 11
        events[1].outcome.return_value = 12
        events[2].outcome.return_value = 13
        self.mock_simple_event.side_effect = events
        space = SampleSpace("H", "T", "S")
        outcomes = space.outcomes()
        for event in events: event.outcome.assert_called_with()
        self.assertEqual(set(outcomes), set([11, 12, 13]))
