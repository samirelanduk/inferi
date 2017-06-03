"""Contains the Value class."""

class Value:
    """A Value represents a numerical measurement of some kind, with its
    associated uncertainty/error.

    :param value: The value."""

    def __init__(self, value):
        if not isinstance(value, (int, float)) or isinstance(value, bool):
            return TypeError("{} is not an int or a float".format(value))
        self._value = value
        self._error = 0
