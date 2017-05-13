"""Contains the base Dataset class."""

class Dataset:

    def __init__(self, *rows):
        """Represents a table of data."""

        try:
            self._rows = [[v for v in row] for row in rows]
        except:
            self._rows = [[row] for row in rows]
        self._x = list(range(len(rows)))
        self._names = [
         "y{}".format(n + 1 if n else "") for n in range(len(self._rows[0]))
        ]
        self._xname = "x"
