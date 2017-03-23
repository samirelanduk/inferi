from unittest import TestCase
from inferi.series import Series
from inferi.exceptions import EmptySeriesError

class SeriesCreationTests(TestCase):

    def test_can_create_series(self):
        series = Series(11, 45, 23, 12, 9)
        self.assertEqual(series._name, None)
        self.assertEqual(series._sample, True)
        self.assertIsInstance(series, list)


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


    def test_can_get_standard_deviation_of_series(self):
        series = Series(5, 7, 1, 2, 4)
        self.assertAlmostEqual(series.standard_deviation(), 2.39, delta=0.005)
