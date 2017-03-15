from unittest import TestCase
from inferi.variables import Variable

class VariableCreationTests(TestCase):

    def test_can_create_variable(self):
        var = Variable(11, 45, 23, 12, 9)
        self.assertIsInstance(var, list)


    def test_can_create_variable_with_name(self):
        var = Variable(11, 45, 23, 12, 9, name="heights")
        self.assertEqual(var._name, "heights")


    def test_name_must_be_str(self):
        with self.assertRaises(TypeError):
            Variable(11, 45, 23, 12, 9, name=100)


    def test_variable_repr(self):
        var = Variable(11, 45, 23, 12, 9)
        self.assertEqual(str(var), "<Variable: [11, 45, 23, 12, 9]>")
        var = Variable(11, 45, 23, 12, 9, name="heights")
        self.assertEqual(str(var), "<'heights': [11, 45, 23, 12, 9]>")
