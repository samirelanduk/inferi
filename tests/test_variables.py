from unittest import TestCase
from inferi.variables import Variable

class VariableCreationTests(TestCase):

    def test_can_create_variable(self):
        var = Variable(11, 45, 23, 12, 9)
        self.assertIsInstance(var, list)
