from unittest import TestCase
from inferi.series import Series
from inferi.exceptions import EmptySeriesError

class SeriesCreationTests(TestCase):

    def test_can_create_series(self):
        series = Series(11, 45, 23, 12, 9)
        self.assertEqual(series._name, None)
        self.assertEqual(series._sample, True)
        self.assertIsInstance(series, list)


    def test_can_make_series_from_list(self):
        series = Series([11, 45, 23, 12, 9])
        self.assertEqual(series[0], 11)
        self.assertEqual(series[1], 45)
        self.assertEqual(series[2], 23)
        self.assertEqual(series[3], 12)
        self.assertEqual(series[4], 9)


    def test_can_make_series_from_tuple(self):
        series = Series((11, 45, 23, 12, 9))
        self.assertEqual(series[0], 11)
        self.assertEqual(series[1], 45)
        self.assertEqual(series[2], 23)
        self.assertEqual(series[3], 12)
        self.assertEqual(series[4], 9)


    def test_can_create_series_with_name(self):
        series = Series(11, 45, 23, 12, 9, name="heights")
        self.assertEqual(series._name, "heights")


    def test_name_must_be_str(self):
        with self.assertRaises(TypeError):
            Series(11, 45, 23, 12, 9, name=100)


    def test_can_create_population_series(self):
        series = Series(11, 45, 23, 12, 9, sample=False)
        self.assertEqual(series._sample, False)


    def test_cannot_have_empty_series(self):
        with self.assertRaises(EmptySeriesError):
            Series()


    def test_series_repr(self):
        series = Series(11, 45, 23, 12, 9)
        self.assertEqual(str(series), "<Series: [11, 45, 23, 12, 9]>")
        series = Series(11, 45, 23, 12, 9, name="heights")
        self.assertEqual(str(series), "<'heights': [11, 45, 23, 12, 9]>")



class SeriesPropertyTests(TestCase):

    def test_series_length(self):
        series = Series(11, 45, 23, 12, 9)
        self.assertEqual(series.length(), 5)


    def test_series_name(self):
        series = Series(11, 45, 23, 12, 9, name="heights")
        self.assertIs(series.name(), series._name)


    def test_can_update_series_name(self):
        series = Series(11, 45, 23, 12, 9, name="heights")
        series.name("weights")
        self.assertEqual(series.name(), "weights")


    def test_series_name_must_be_str(self):
        series = Series(11, 45, 23, 12, 9)
        with self.assertRaises(TypeError):
            series.name(100)


    def test_series_sample(self):
        series = Series(11, 45, 23, 12, 9, sample=False)
        self.assertIs(series.sample(), series._sample)


    def test_can_update_series_sample(self):
        series = Series(11, 45, 23, 12, 9, sample=False)
        series.sample(True)
        self.assertEqual(series.sample(), True)


    def test_series_sample_must_be_bool(self):
        series = Series(11, 45, 23, 12, 9)
        with self.assertRaises(TypeError):
            series.sample("100")



class SeriesModificationTests(TestCase):

    def test_cannot_remove_last_item_from_series(self):
        series = Series(11, 45)
        series.remove(11)
        with self.assertRaises(EmptySeriesError):
            series.remove(45)


    def test_cannot_pop_last_item_from_series(self):
        series = Series(11, 45)
        series.pop()
        with self.assertRaises(EmptySeriesError):
            series.pop()



class SeriesCentralityTests(TestCase):

    def test_can_get_series_mean(self):
        series = Series(11, 45, 23, 12, 10)
        self.assertEqual(series.mean(), 20.2)


    def test_can_get_odd_series_median(self):
        series = Series(11, 45, 23, 12, 10)
        self.assertEqual(series.median(), 12)


    def test_can_get_even_series_median(self):
        series = Series(11, 45, 23, 12, 10, 15)
        self.assertEqual(series.median(), 13.5)


    def test_can_get_series_mode(self):
        series = Series(11, 45, 23, 12, 10, 11, 23, 11)
        self.assertEqual(series.mode(), 11)


    def test_mode_returns_none_when_multi_modal(self):
        series = Series(11, 45, 23, 12, 10, 11, 23)
        self.assertIs(series.mode(), None)



class SeriesDispersionTests(TestCase):

    def test_can_get_series_range(self):
        series = Series(11, 45, 23, 12, 10, -15)
        self.assertEqual(series.range(), 60)


    def test_can_get_variance(self):
        series = Series(5, 7, 1, 2, 4)
        self.assertEqual(series.variance(), 5.7)


    def test_can_get_population_variance(self):
        series = Series(5, 7, 1, 2, 4, sample=False)
        self.assertAlmostEqual(series.variance(), 4.56, delta=0.005)


    def test_can_get_standard_deviation(self):
        series = Series(5, 7, 1, 2, 4)
        self.assertAlmostEqual(series.standard_deviation(), 2.39, delta=0.005)


    def test_can_get_population_standard_deviation(self):
        series = Series(5, 7, 1, 2, 4, sample=False)
        self.assertAlmostEqual(series.standard_deviation(), 2.135, delta=0.005)


    def test_can_get_z_scores_of_values_in_series(self):
        series = Series(7, 8, 8, 7.5, 9)
        self.assertAlmostEqual(series.z_score(7.5), -0.54, delta=0.005)


    def test_can_get_standard_error_of_mean(self):
        series = Series(10, 20, 30, 40, 50)
        self.assertAlmostEqual(series.standard_error_mean(), 7.0711, delta=0.005)



class SeriesComparisonTests(TestCase):

    def test_can_get_covariance_between_series(self):
        series1 = Series(2.1, 2.5, 4.0, 3.6)
        series2 = Series(8, 12, 14, 10)
        self.assertAlmostEqual(series1.covariance_with(series2), 1.53, delta=0.005)
        self.assertAlmostEqual(series2.covariance_with(series1), 1.53, delta=0.005)


    def test_can_only_get_covariance_with_other_series(self):
        series1 = Series(2.1, 2.5, 4.0, 3.6)
        series2 = [8, 12, 14, 10]
        with self.assertRaises(TypeError):
            series1.covariance_with(series2)


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


    def test_can_only_get_correlation_with_other_series(self):
        series1 = Series(2.1, 2.5, 4.0, 3.6)
        series2 = [8, 12, 14, 10]
        with self.assertRaises(TypeError):
            series1.correlation_with(series2)


    def test_correlation_requires_other_series_to_be_same_length(self):
        series1 = Series(2.1, 2.5, 4.0, 3.6)
        series2 = Series(8, 12, 10)
        with self.assertRaises(ValueError):
            series1.correlation_with(series2)
