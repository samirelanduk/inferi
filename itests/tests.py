from unittest import TestCase
from inferi.series import Series

class Tests(TestCase):

    def test_can_get_variance(self):
        series = Series(5, 7, 1, 2, 4)
        self.assertEqual(series.variance(), 5.7)


    def test_can_get_population_variance(self):
        series = Series(5, 7, 1, 2, 4, sample=False)
        self.assertAlmostEqual(series.variance(), 4.56, delta=0.005)


    def test_can_get_standard_deviation(self):
        series = Series(5, 7, 1, 2, 4)
        self.assertAlmostEqual(series.standard_deviation(), 2.39, delta=0.005)


    def test_can_get_z_scores_of_values_in_series(self):
        series = Series(7, 8, 8, 7.5, 9)
        self.assertAlmostEqual(series.z_score(7.5), -0.54, delta=0.005)


    def test_can_get_standard_error_of_mean(self):
        series = Series(10, 20, 30, 40, 50)
        self.assertAlmostEqual(series.standard_error_mean(), 7.0711, delta=0.005)


    def test_can_get_covariance_between_series(self):
        series1 = Series(2.1, 2.5, 4.0, 3.6)
        series2 = Series(8, 12, 14, 10)
        self.assertAlmostEqual(series1.covariance_with(series2), 1.53, delta=0.005)
        self.assertAlmostEqual(series2.covariance_with(series1), 1.53, delta=0.005)


    def test_covariance_requires_other_series_to_be_same_length(self):
        series1 = Series(2.1, 2.5, 4.0, 3.6)
        series2 = Series(8, 12, 10)
        with self.assertRaises(ValueError):
            series1.covariance_with(series2)


    def test_can_get_correlation_between_series(self):
        series1 = Series(2.1, 2.5, 4.0, 3.6)
        series2 = Series(8, 12, 14, 10)
        self.assertAlmostEqual(series1.correlation_with(series2), 0.66, delta=0.005)
        self.assertAlmostEqual(series2.correlation_with(series1), 0.66, delta=0.005)
