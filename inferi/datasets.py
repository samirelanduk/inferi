"""Contains the base Dataset class."""

class Dataset:

    def __init__(self, *rows, x=None, name="y", names=None):
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

        self._x = x or list(range(len(rows)))
        if len(self._x) != len(self._rows):
            raise ValueError("x values ({}) must be same length as rows ({})".format(
             len(self._x), len(self._rows)
            ))
        if not isinstance(name, str):
            raise TypeError("name '{}' is not a str".format(name))
        if names:
            for name in names:
                if not isinstance(name, str):
                    raise TypeError("name '{}' is not a str".format(name))
            if len(names) != len(self._rows[0]):
                raise ValueError("{} names given for {} columns".format(
                 len(names), len(self._rows[0]))
                )
            self._names = names
        else:
            self._names = [
             "{}{}".format(name, n + 1 if n else "") for n in range(len(self._rows[0]))
            ]
        self._xname = "x"
