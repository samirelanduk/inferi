"""Contains the base Data class."""

from .exceptions import DuplicateXError

class Data:
    """Represents a list of measurements.

    :param \*values: The values that make up the data."""

    def __init__(self, *values, name="y", xname="x"):
        try:
            if str in [type(v) for v in values]: raise TypeError
            self._values = [[index, value] for index, value in values]
            if len(set([v[0] for v in values])) != len([v[0] for v in values]):
                raise DuplicateXError(
                 "{} contains duplicate x values".format(values)
                )
        except ValueError:
            raise ValueError("Iterable values can only be of length 2")
        except TypeError:
            self._values = [[index, value] for index, value in enumerate(values)]
        if not isinstance(name, str):
            raise TypeError("name '{}' is not a str".format(name))
        self._name = name
        if not isinstance(xname, str):
            raise TypeError("xname '{}' is not a str".format(xname))
        self._xname = xname


    def __repr__(self):
        if self._name == "y":
            return "<Data {}>".format(tuple([val[1] for val in self._values]))
        return "<Data '{}' {}>".format(
         self._name, tuple([val[1] for val in self._values])
        )


    def __len__(self):
        return len(self._values)


    def __contains__(self, member):
        for x, y in self._values:
            if y == member: return True
        return False


    def __iter__(self):
        return iter([val[1] for val in self._values])


    def __getitem__(self, key):
        for x, y in self._values:
            if x == key: return y
        raise IndexError("{} has no x value {}".format(self, key))


    def __setitem__(self, key, y):
        for index, value in enumerate(self._values):
            if value[0] == key:
                self._values[index][1] = y
                return
        self._values.append([key, y])
