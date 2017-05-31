"""This module contains the Sample class."""

from collections import Counter
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


    def median(self):
        """Returns the median y value - the value that occurs midway through
        when the y values are sorted. If there is an even number, the midpoint
        between the two median values will be returned."""

        values = sorted(self.values())
        if len(values) % 2:
            return values[int((len(values) - 1) / 2)]
        midway = int(self.length() / 2)
        return (values[midway - 1] + values[midway]) / 2


    def mode(self):
        """Returns the mode y value - the value that occurs the most often. If
        more than one value meets this criteria, ``None`` is returned."""

        values = Counter(self.values())
        highest_frequency = max(values.values())
        if len([v for v in values if values[v] == highest_frequency]) == 1:
            return values.most_common()[0][0]


    def range(self):
        """Returns the range of the y values - the difference between the
        largest and smallest values."""

        return self.max() - self.min()
