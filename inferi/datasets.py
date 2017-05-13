"""Contains the base Dataset class."""

class Dataset:

    def __init__(self, *rows):
        """Represents a table of data."""

        try:
            self._rows = [[v for v in row] for row in rows]
            if len(set([len(row) for row in self._rows])) != 1:
                wrong_row = [
                 row for row in self._rows if len(row) != len(self._rows[0])
                ][0]
                raise ValueError(
                 "Rows must be of equal length - '{}' invalid".format(wrong_row)
                )
        except TypeError:
            self._rows = [[row] for row in rows]
        self._x = list(range(len(rows)))
        self._names = [
         "y{}".format(n + 1 if n else "") for n in range(len(self._rows[0]))
        ]
        self._xname = "x"
