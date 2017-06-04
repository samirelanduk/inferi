"""Contains the Value class."""

class Value:
    """A Value represents a numerical measurement of some kind, with its
    associated uncertainty/error.

    For example a value of 23 ± 0.2 would be ``Value(23, 0.2)``

    :param value: The value.
    :param error: The uncertainty associated with the value. By default this is\
    zero.
    :raises TypeError: if either the value or its error is not numeric."""

    def __init__(self, value, error=0):
        if not isinstance(value, (int, float)) or isinstance(value, bool):
            return TypeError("value {} is not an int or a float".format(value))
        if not isinstance(error, (int, float)) or isinstance(error, bool):
            return TypeError("error {} is not an int or a float".format(error))
        if error < 0:
            raise ValueError("error {} is negative".format(error))
        self._value = value
        self._error = error


    def __repr__(self):
        if self._error:
            return "{} ± {}".format(self._value, self._error)
        return str(self._value)


    def __add__(self, other):
        value = self._value + (other._value if isinstance(other, Value) else other)
        error = self._error + (other._error if isinstance(other, Value) else 0)
        return Value(value, error)


    def __radd__(self, other):
        return self + other


    def __sub__(self, other):
        value = self._value - (other._value if isinstance(other, Value) else other)
        error = self._error + (other._error if isinstance(other, Value) else 0)
        return Value(value, error)


    def __rsub__(self, other):
        value = (other._value if isinstance(other, Value) else other) - self._value
        error = self._error + (other._error if isinstance(other, Value) else 0)
        return Value(value, error)


    def value(self):
        """Returns the value's... value. That is, the measurement itself,
        without its associated error.

        :rtype: ``int`` or ``float``"""

        return self._value


    def error(self):
        """Returns the value's associated error.

        :rtype: ``int`` or ``float``"""

        return self._error


    def relative_error(self):
        """Returns the value's associated error as a proportion of the value.

        :rtype: ``float``"""

        return self._error / self._value
