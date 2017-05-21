"""Contains the base Data class."""

class Data:
    """Represents a list of measurements.

    :param \*values: The values that make up the data."""

    def __init__(self, *values):
        try:
            if str in [type(v) for v in values]: raise TypeError
            self._values = [[index, value] for index, value in values]
        except ValueError:
            raise ValueError("Iterable values can only be of length 2")
        except TypeError:
            self._values = [[index, value] for index, value in enumerate(values)]
