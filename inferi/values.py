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
        self._value = value
        self._error = error


    def __repr__(self):
        if self._error:
            return "{} ± {}".format(self._value, self._error)
        return str(self._value)
