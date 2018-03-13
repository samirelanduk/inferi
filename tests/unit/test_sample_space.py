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



class SampleSpaceChancesOfTests(SampleSpaceTest):

    def test_can_get_chances_of(self):
        space = SampleSpace("H", "T")
        self.assertEqual(space.chances_of("H"), 0.33)
        self.simple_events[0].outcome.assert_called_with()
        self.simple_events[0].probability.assert_called_with()



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
