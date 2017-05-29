"""This module contains the Sample class."""

from .data import Data

class Sample(Data):
    """Base class: :py:class:`.Data`

    A sample is an unordered collection of (x, y) value pairs, typically used to
    represent measurements made on some sample or population. For example, the
    heights of children in a class might be represented with:

    ``sample = Sample(("Sally", 123), ("John", 143), ("Meredith", 101))``

    or even just:

    ``sample = Sample(123, 143, 101)``

    You can provide a list (or tuple, or set - any iterable other than string)
    of values, and these will become the y values of the data, with the input x
    values being 0-based indices. Alternatively, you can provide a list of
    length-2 lists (or tuples etc.) and *these* will be interpreted as xy pairs.

    A ``Sample`` object is a container of its y values, is iterable (stepping
    through it will step through its y values), and its x values are accessed
    using square brackets like a dictionary, with the corresponding x-value
    being the key.

    You can delete a value using ``del sample[x_value]`` notation.

    :param \*values: The values that make up the sample.
    :param str name: The name of the y-values.
    :param str xname: The name of the x-values."""

    def sum(self):
        """Returns the sum of the y values in the Sample. This will usually be
        a number but depends on the object types in the Sample."""

        return sum(self)


    def mean(self):
        """Returns the mean of the y values - their sum divided by the number of
        values."""
        
        return self.sum() / self.length()
