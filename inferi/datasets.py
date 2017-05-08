"""Contains the base Dataset class."""

class Dataset:
    """Represents a table of data.

    :param \*rows: The rows of data that make up the Dataset."""

    def __init__(self, *rows):
        self._data = {index: value for index, value in enumerate(rows)}


    def __repr__(self):
        return "<Dataset {}>".format(tuple(self._data.values()))


    def __len__(self):
        return len(self._data)
