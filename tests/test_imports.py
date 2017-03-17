from unittest import TestCase
import inferi

class SeriesImportTests(TestCase):

    def test_series_class_imported(self):
        from inferi.series import Series
        self.assertIs(Series, inferi.Series)
