"""Contains the base Dataset class."""

class Dataset:

    def __init__(self, *rows, x=None, name="y", names=None, x_name="x"):
        """Represents a table of data.

        :param \* rows: The rows of data in the dataset. If all the rows are\
        iterable, then these will be interpreted as multi-column data.\
        Otherwise each value will be assumed to be a value in a single column.
        :param x: The names of the input values. If nothing is given, these \
        will just be zero-indexed numbers.
        :param str name: The name of the first column - defaults to ``"y"``.\
        The names of subsequent columns, if there are any, will be based on\
        this. So if the first column is 'y', the second will be 'y2', and so on.
        :param names: The names of all the columns in the data. This overrides\
        parameter ``name`` if both are given.
        :param str x_name: The name of the inputs. Defaults to ``"x"``.
        :raises ValueError: if rows of differing length are given.
        :raises ValueError: if the number of x values given doesn't match the\
        number of rows.
        :raises TypeError: if any of the column names are not strings.
        :raises ValueError: if the number of column names doesn't match the\
        number of columns."""

        # Build rows
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

        # Assign x value names
        self._x = x or list(range(len(rows)))
        if len(self._x) != len(self._rows):
            raise ValueError("x values ({}) must be same length as rows ({})".format(
             len(self._x), len(self._rows)
            ))

        # Determine column names
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
        if not isinstance(x_name, str):
            raise TypeError("x_name '{}' is not a str".format(x_name))
        self._xname = x_name
