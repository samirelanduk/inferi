"""Contains the base Dataset class."""

class Dataset:

    def __init__(self, *rows):
        """Represents a table of data."""

        self._rows = [[row] for row in rows]
        self._x = list(range(len(rows)))
        self._names = ["y1"]
        self._xname = "x"
