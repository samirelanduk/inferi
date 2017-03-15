"""Contains the basic Variable class and its methods."""

class Variable(list):
    """A Variable represents a set of measurements made on a collection of
    entities, such as the heights of a group of football players, or the
    favourite colours of a class of school children.

    It is basically an extended list.

    :param \*values: The measurements, as positional arguments.
    :param str name: The name of this measurement."""

    def __init__(self, *values, name=None, **kwargs):
        list.__init__(self, [*values], **kwargs)

        if not isinstance(name, str) and name is not None:
            raise TypeError("Variable name must be str, not '%s'" % str(name))
        self._name = name


    def __repr__(self):
        if self._name:
            return "<'%s': %s>" % (self._name, list.__repr__(self))
        else:
            return "<Variable: %s>" % list.__repr__(self)


    def length(self):
        """Returns the number of measurements in this variable.

        :rtype: ``int``"""

        return len(self)


    def name(self, name=None):
        """Returns the Variable's name. If an argument is given, the name will
        be set to that value.

        :param str name: The new name of this measurement to set.
        :rtype: ``str``"""
        
        if name is None:
            return self._name
        else:
            if not isinstance(name, str):
                raise TypeError(
                 "Variable name must be str, not '%s'" % str(name)
                )
            self._name = name
