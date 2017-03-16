"""Contains the basic Series class and its methods."""

from collections import Counter

class Series(list):
    """A Series represents a set of measurements made on a collection of
    entities, such as the heights of a group of football players, or the
    favourite colours of a class of school children.

    It is basically an extended list.

    :param \*values: The measurements, as positional arguments.
    :param str name: The name of this set of measurement."""

    def __init__(self, *values, name=None, **kwargs):
        list.__init__(self, [*values], **kwargs)

        if not isinstance(name, str) and name is not None:
            raise TypeError("Series name must be str, not '%s'" % str(name))
        self._name = name


    def __repr__(self):
        if self._name:
            return "<'%s': %s>" % (self._name, list.__repr__(self))
        else:
            return "<Series: %s>" % list.__repr__(self)


    def length(self):
        """Returns the number of measurements in this series.

        :rtype: ``int``"""

        return len(self)


    def name(self, name=None):
        """Returns the Series's name. If an argument is given, the name will
        be set to that value.

        :param str name: The new name of this measurement to set.
        :rtype: ``str``"""

        if name is None:
            return self._name
        else:
            if not isinstance(name, str):
                raise TypeError(
                 "Series name must be str, not '%s'" % str(name)
                )
            self._name = name


    def mean(self):
        return sum(self) / len(self)


    def median(self):
        sorted_values = sorted(self)
        if self.length() % 2:
            return sorted_values[int((self.length() / 2) - 0.5)]
        else:
            midway = int(self.length() / 2)
            return (sorted_values[midway - 1] + sorted_values[midway]) / 2


    def mode(self):
        values = Counter(self)
        highest_frequency = max(values.values())
        modes = [value for value in values if values[value] == highest_frequency]
        if len(modes) == 1:
            return modes[0]
