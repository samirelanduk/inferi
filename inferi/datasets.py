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
            if variable.length() != variables[0].length():
                raise ValueError(
                 "Can't make Dataset with different-length Variables"
                )
        self._variables = list(variables)


    def __repr__(self):
        return "<Dataset ({} Variables)>".format(len(self._variables))


    def __getitem__(self, index):
        return self._variables[index]


    def variables(self):
        """Returns the :py:class:`.Variable` objects in the Dataset.

        :rtype: ``tuple``"""

        return tuple(self._variables)
