from unittest import TestCase
from unittest.mock import Mock, patch
from inferi.probability import SampleSpace

class SampleSpaceTest(TestCase):

    def setUp(self):
        self.patch1 = patch("inferi.probability.SimpleEvent")
        self.mock_simple_event = self.patch1.start()
        self.simple_events = [Mock(), Mock(), Mock()]
        self.simple_events[0].outcome.return_value = "H"
        self.simple_events[1].outcome.return_value = "T"
        self.simple_events[2].outcome.return_value = "S"
        self.simple_events[0].probability.return_value = 0.33
        self.simple_events[1].probability.return_value = 0.33
        self.simple_events[2].probability.return_value = 0.33
        self.mock_simple_event.side_effect = self.simple_events


    def tearDown(self):
        self.patch1.stop()



class SampleSpaceCreationTests(SampleSpaceTest):

    def test_can_create_sample_space(self):
        space = SampleSpace("H", "T")
        self.assertEqual(space._simple_events, set(self.simple_events[:2]))
        self.mock_simple_event.assert_any_call("H", 0.5)
        self.mock_simple_event.assert_any_call("T", 0.5)



class SampleSpaceReprTests(SampleSpaceTest):

    def test_sample_space_repr(self):
        space = SampleSpace("H", "T")
        self.assertEqual(str(space), "<SampleSpace (2 simple events)>")



class SampleSpaceContainerTests(SampleSpaceTest):

    def test_can_look_for_simple_events(self):
        space = SampleSpace("H", "T")
        self.assertIn(self.simple_events[0], space)
        self.assertIn(self.simple_events[1], space)
        self.assertNotIn(self.simple_events[2], space)


    @patch("inferi.probability.SampleSpace.outcomes")
    def test_can_look_for_outcomes(self, mock_outcomes):
        mock_outcomes.return_value = [1, 2]
        space = SampleSpace("H", "T")
        self.assertIn(1, space)
        self.assertIn(2, space)
        self.assertNotIn(3, space)
        mock_outcomes.assert_called_with()



class SampleSpaceSimpleEvents(SampleSpaceTest):

    def test_sample_space_simple_events(self):
        space = SampleSpace("H", "T")
        self.assertEqual(space.simple_events(), space._simple_events)
        self.assertIsNot(space.simple_events(), space._simple_events)



class SampleSpaceOutcomesTests(SampleSpaceTest):

    def test_can_get_outcomes(self):
        space = SampleSpace("H", "T", "S")
        outcomes = space.outcomes()
        for event in self.simple_events: event.outcome.assert_called_with()
        self.assertEqual(set(outcomes), set(["H", "T", "S"]))



class SampleSpaceEventTests(SampleSpaceTest):

    def test_can_get_event(self):
        space = SampleSpace("H", "T", "S")
        self.assertIs(space.event("H"), self.simple_events[0])
        self.assertIs(space.event("S"), self.simple_events[2])


    def test_can_return_no_event(self):
        space = SampleSpace("H", "T", "S")
        self.assertIsNone(space.event("A"))



class SampleSpaceChancesOfTests(SampleSpaceTest):

    @patch("inferi.probability.SampleSpace.event")
    def test_can_get_chances_of(self, mock_event):
        mock_event.return_value = self.simple_events[0]
        space = SampleSpace("H", "T")
        self.assertEqual(space.chances_of("H"), 0.33)
        mock_event.assert_called_with("H")
        self.simple_events[0].probability.assert_called_with()


    @patch("inferi.probability.SampleSpace.event")
    def test_can_get_chances_of_no_event(self, mock_event):
        mock_event.return_value = None
        space = SampleSpace("H", "T")
        self.assertEqual(space.chances_of("H"), 0)
        mock_event.assert_called_with("H")



class SampleSpaceExperimentTests(SampleSpaceTest):

    def setUp(self):
        SampleSpaceTest.setUp(self)
        self.patch1 = patch("inferi.probability.SampleSpace.outcomes")
        self.mock_outcomes = self.patch1.start()
        self.mock_outcomes.return_value = set(["H", "T"])


    def tearDown(self):
        self.patch1.stop()


    def test_can_run_statistical_experiment(self):
        space = SampleSpace("H", "T")
        results = [space.experiment() for _ in range(100)]
        self.assertEqual(set(results), set(["H", "T"]))
        self.assertGreaterEqual(results.count("H"), 35)
        self.assertGreaterEqual(results.count("T"), 35)
        self.mock_outcomes.assert_called_with()
