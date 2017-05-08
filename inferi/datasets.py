"""Contains the base Dataset class."""

class Dataset:
    """Represents a table of data.

    Datasets are containers of their values, and are also iterable, allowing you
    to step through them line by line.

    :param \*rows: The rows of data that make up the Dataset."""

    def __init__(self, *rows):
        self._data = {index: value for index, value in enumerate(rows)}


    def __repr__(self):
        return "<Dataset {}>".format(tuple(self._data.values()))


    def __len__(self):
        return len(self._data)


    def __contains__(self, member):
        return member in self._data.values()


    def __iter__(self):
        return iter(self._data.values())


    def __getitem__(self, index):
        return self._data[index]


    def __setitem__(self, index, value):
        self._data[index] = value
