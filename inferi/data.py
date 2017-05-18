"""Contains the base Data class."""

class Data:
    """Represents a list of measurements.

    :param \*values: The values that make up the data."""

    def __init__(self, *values):
        self._values = [[index, value] for index, value in enumerate(values)]
