"""Contains the base Dataset class."""

class Dataset:
    """Represents a table of data.

    :param \*rows: The rows of data that make up the Dataset."""

    def __init__(self, *rows):
        self._data = {index: value for index, value in enumerate(rows)}