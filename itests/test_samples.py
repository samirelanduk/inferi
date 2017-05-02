from unittest import TestCase
from inferi import Sample

class SampleTests(TestCase):

    def test_sample_handling(self):
        sample = Sample(4, 8, 15, 16, 23, 42)
        self.assertEqual(sample.length(), 6)
        self.assertEqual(sample.data(), (4, 8, 15, 16, 23, 42))

        sample.add(108)
        self.assertEqual(sample.length(), 7)
        self.assertEqual(sample.data(), (4, 8, 15, 16, 23, 42, 108))

        sample.remove(23)
        sample.remove(8)
        self.assertEqual(sample.length(), 5)
        self.assertEqual(sample.data(), (4, 15, 16, 23, 108))


    def test_sample_centrality(self):
        sample = Sample(13, 18, 13, 14, 13, 16, 14, 21, 13)
        self.assertEqual(sample.mean(), 15)
        self.assertEqual(sample.median(), 14)
        self.assertEqual(sample.mode(), 13)

        sample.remove(13)
        sample.remove(13)
        self.assertEqual(sample.mode(), None)
        sample.remove(13)
        self.assertEqual(sample.model(), 14)


    def test_sample_dispersion(self):
        sample = Sample(600, 470, 170, 430, 300)
        self.assertEqual(sample.variance(), 27130)
        self.assertAlmostEqual(sample.st_dev(), 164.71, delta=0.01)
        self.assertAlmostEqual(sample.st_err(), 73.66, delta=0.01)

        sample = Sample(population=True)
        self.assertEqual(sample.variance(), 21704)
        self.assertAlmostEqual(sample.st_dev(), 147.32, delta=0.01)


    def test_sample_z_scores(self):
        sample = Sample(7, 8, 8, 7.5, 9)
        self.assertAlmostEqual(sample.z_score(7.5), -0.54, delta=0.005)


    def test_sample_correlation(self):
        sample1 = Sample(2.1, 2.5, 4.0, 3.6)
        sample2 = Sample(8, 12, 14, 10)
        self.assertAlmostEqual(sample1.covariance_with(sample2), 1.53, delta=0.005)
        self.assertAlmostEqual(sample2.covariance_with(sample1), 1.53, delta=0.005)
        self.assertAlmostEqual(sample1.correlation_with(sample2), 0.66, delta=0.005)
        self.assertAlmostEqual(sample2.correlation_with(sample1), 0.66, delta=0.005)
        sample1.add(10)
        with self.assertRaises(ValueError):
            sample1.covariance_with(sample2)
        with self.assertRaises(ValueError):
            sample1.correlation_with(sample2)
