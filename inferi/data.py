"""Contains the base Data class."""

from .exceptions import DuplicateXError

class Data:
    """Represents a list of measurements, as x-value, y-value pairs. Generally
    this class would not be instantiated directly, but is here to act as a
    parent class for others.

    You can provide a list (or tuple, or set - any collection other than string)
    of values, and these will become the y values of the data, with the input x
    values being 0-based indices. Alternatively, you can provide a list of
    length-2 lists (or tuples etc.) and *these* will be interpreted as xy pairs.

    A ``Data`` object is a container of its y values, is iterable (stepping
    through it will step through its y values), and its x values are accessed
    using square brackets like a dictionary, with the corresponding x-value
    being the key.

    You can delete a value using ``del data[x_value]`` notation.

    :param \*values: The values that make up the data.
    :param str name: The name of the y-values.
    :param str xname: The name of the x-values."""


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


    def __delitem__(self, key):
        for index, value in enumerate(self._values):
            if value[0] == key:
                self._values.pop(index)
                return


    def values(self, x=False):
        """Returns the values in the Data. By default only the y (output) values
        are returned. To return the values as (x, y) pairs, set the ``x``
        argument to ``True``.

        :param bool x: If True, the x values will also be included with the y\
        values.
        :rtype: ``tuple``"""

        if x:
            return tuple([(x, y) for x, y in self._values])
        else:
            return tuple([y for x, y in self._values])


    def name(self, name=None):
        """Returns the name of the y-values in the Data. If a value is given,
        the name will be updated to this (provided it is a string).

        :param str name: If given, this will be made the new name.
        :raises TypeError: if the name given is not a string."""

        if name is None:
            return self._name
        else:
            if not isinstance(name, str):
                raise TypeError("name '{}' is not a str".format(name))
            self._name = name


    def xname(self, xname=None):
        """Returns the name of the x-values in the Data. If a value is given,
        the xname will be updated to this (provided it is a string).

        :param str xname: If given, this will be made the new xname.
        :raises TypeError: if the xname given is not a string."""

        if xname is None:
            return self._xname
        else:
            if not isinstance(xname, str):
                raise TypeError("xname '{}' is not a str".format(xname))
            self._xname = xname
