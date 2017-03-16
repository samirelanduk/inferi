from unittest import TestCase
from inferi.series import Series

class SeriesCreationTests(TestCase):

    def test_can_create_series(self):
        series = Series(11, 45, 23, 12, 9)
        self.assertIsInstance(series, list)


    def test_can_create_series_with_name(self):
        series = Series(11, 45, 23, 12, 9, name="heights")
        self.assertEqual(series._name, "heights")


    def test_name_must_be_str(self):
        with self.assertRaises(TypeError):
            Series(11, 45, 23, 12, 9, name=100)


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
