"""Contains the base Data class."""

class Data:
    """Represents a list of measurements.

    :param \*values: The values that make up the data."""

    def __init__(self, *values, name="y", xname="x"):
        try:
            if str in [type(v) for v in values]: raise TypeError
            self._values = [[index, value] for index, value in values]
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
