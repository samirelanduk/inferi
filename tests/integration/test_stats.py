from unittest import TestCase
import inferi

class Tests(TestCase):

    def test_variables(self):
        # Basic variable behaviour
        var = inferi.Variable(4, 8, 15, 16, 23, 42, name="Numbers")
        self.assertEqual(var.values(), (4, 8, 15, 16, 23, 42))
        self.assertEqual(var.name(), "Numbers")
        self.assertEqual(len(var), 6)
        self.assertEqual(var.length(), 6)
        var[4] = 24
        self.assertEqual(var.values(), (4, 8, 15, 16, 24, 42))
        var[4] = 23
        self.assertEqual(var[4], 23)
        var.set(2, 14)
        self.assertEqual(var.values(), (4, 8, 14, 16, 23, 42))
        var.set(2, 15)
        self.assertEqual(var.get(2), 15)
        var.add(108)
        self.assertEqual(var.values(), (4, 8, 15, 16, 23, 42, 108))
        var.remove(108)
        self.assertEqual(var.values(), (4, 8, 15, 16, 23, 42))
        self.assertEqual(var.pop(), 42)
        self.assertEqual(var.values(), (4, 8, 15, 16, 23))
        var.add(42)
        self.assertEqual(var[-1], 42)
        var.name("The Numbers")
        self.assertEqual(var.name(), "The Numbers")

        # Variable metrics
        self.assertEqual(var.min(), 4)
        self.assertEqual(var.max(), 42)
        self.assertEqual(var.sum(), 108)
        self.assertEqual(var.mean(), 18)
        self.assertEqual(var.median(), 15.5)
        self.assertEqual(var.mode(), None)
        var.add(15)
        self.assertEqual(var.mode(), 15)
        var.pop()
        self.assertEqual(var.range(), 38)
        self.assertAlmostEqual(var.variance(), 182, delta=0.005)
        self.assertAlmostEqual(var.variance(population=True), 151.67, delta=0.005)
        self.assertAlmostEqual(var.st_dev(), 13.49, delta=0.005)
        self.assertAlmostEqual(var.st_dev(population=True), 12.32, delta=0.005)
        self.assertAlmostEqual(var.zscore(4.51), -1, delta=0.005)

        # Variable comparison
        var2 = inferi.Variable(34, 21, 56, 43, 78, 79)
        self.assertAlmostEqual(var.covariance_with(var2), 269.2, delta=0.05)
        self.assertAlmostEqual(var.correlation_with(var2), 0.845, delta=0.005)

        # Variable arithmetic
        var3 = inferi.Variable.average(var, var2)
        self.assertEqual(var3.length(), 6)
        self.assertEqual(var3[0], 19)
        self.assertEqual(var3[2], 35.5)
        var3 = var + var2
        self.assertEqual(var3.length(), 6)
        self.assertEqual(var3[0], 38)
        self.assertEqual(var3[2], 71)
        var3 = var2 - var
        self.assertEqual(var3.length(), 6)
        self.assertEqual(var3[0], 30)
        self.assertEqual(var3[2], 41)

        # Variable errors
        var = inferi.Variable(4, 8, 15, name="Numbers", error=[0.8, 0.5, 0.3])
        self.assertEqual(var.values(), (4, 8, 15))
        self.assertEqual(var.error(), (0.8, 0.5, 0.3))
        self.assertEqual(var.get(0), 4)
        self.assertEqual(var.get(0, error=True).error(), 0.8)
        self.assertEqual(var.get(0, error=True).relative_error(), 0.2)


    def test_datasets(self):
        v1 = inferi.Variable("Stannis", "Joffrey", "Renly", "Robb", name="name")
        v2 = inferi.Variable(
         1.86, 1.56, 1.79, 1.81, error=[0.1, 0.2, 0.3, 0.4], name="height"
        )
        v3 = inferi.Variable(False, True, False, False, name="illegitimate")
        v4 = inferi.Variable(36, 15, 32, 16, name="age")

        dataset = inferi.Dataset(v1, v2, v3, v4)
        self.assertEqual(dataset.variables(), (v1, v2, v3, v4))
        self.assertEqual(len(dataset.rows()), 4)
        self.assertEqual(dataset.rows()[0], ("Stannis", 1.86, False, 36))

        v5 = inferi.Variable(1, 2, 1, 4, name="siblings")
        dataset.add_variable(v5)
        v6 = inferi.Variable(
         "Baratheon", "Lannister", "Baratheon", "Stark", name="house"
        )
        dataset.insert_variable(1, v6)
        self.assertEqual(dataset.variables(), (v1, v6, v2, v3, v4, v5))
        dataset.remove_variable(v3)
        v = dataset.pop_variable()
        self.assertIs(v, v5)
        self.assertEqual(dataset.variables(), (v1, v6, v2, v4))

        dataset.sort()
        self.assertEqual(v1.values(), ("Joffrey", "Renly", "Robb", "Stannis"))
        self.assertEqual(v6.values(), ("Lannister", "Baratheon", "Stark", "Baratheon"))
        self.assertEqual(v2.values(), (1.56, 1.79, 1.81, 1.86))
        self.assertEqual(v2.error(), (0.2, 0.3, 0.4, 0.1))
        self.assertEqual(v4.values(), (15, 32, 16, 36))

        dataset.sort(v4)
        self.assertEqual(v1.values(), ("Joffrey", "Robb", "Renly", "Stannis"))
        self.assertEqual(v6.values(), ("Lannister", "Stark", "Baratheon", "Baratheon"))
        self.assertEqual(v2.values(), (1.56, 1.81, 1.79, 1.86))
        self.assertEqual(v2.error(), (0.2, 0.4, 0.3, 0.1))
        self.assertEqual(v4.values(), (15, 16, 32, 36))

        dataset.add_row(["Jon", "Snow", 1.79, 15])
        self.assertEqual(
         v1.values(), ("Joffrey", "Robb", "Renly", "Stannis", "Jon")
        )
