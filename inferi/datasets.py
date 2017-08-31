"""Contains the Dataset class."""

from .variables import Variable

class Dataset:
    """A collection of :py:class:`.Variable` objects which describe the same
    experimental units.

    :param \*variables: The Variables that make up the Dataset.
    :raises TypeError: if non-Variables are given."""

    def __init__(self, *variables):
        for variable in variables:
            if not isinstance(variable, Variable):
                raise TypeError("{} is not a Variable".format(variable))
        self._variables = list(variables)
