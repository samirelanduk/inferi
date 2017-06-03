"""Contains the Value class."""

class Value:
    """A Value represents a numerical measurement of some kind, with its
    associated uncertainty/error.

    :param value: The value."""

    def __init__(self, value):
        self._value = value
        self._error = 0
