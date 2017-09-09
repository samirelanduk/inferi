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


    def add_variable(self, variable):
        """Adds a :py:class:`.Variable` column to the Dataset.

        :param Variable variable: The Variable to add.
        :raises TypeError: if a non-Variable is given.
        :raises ValueError: if the Variable's length doesn't match."""

        if not isinstance(variable, Variable):
            raise TypeError("{} is not a Variable".format(variable))
        if self._variables and variable.length() != self._variables[0].length():
            raise ValueError(
             "Can't have Dataset with different-length Variables"
            )
        self._variables.append(variable)


    def insert_variable(self, index, variable):
        """Inserts a :py:class:`.Variable` column to the Dataset at the index
        given..

        :param int index: The location to insert at.
        :param Variable variable: The Variable to add.
        :raises TypeError: if a non-Variable is given.
        :raises ValueError: if the Variable's length doesn't match."""

        if not isinstance(variable, Variable):
            raise TypeError("{} is not a Variable".format(variable))
        if self._variables and variable.length() != self._variables[0].length():
            raise ValueError(
             "Can't have Dataset with different-length Variables"
            )
        self._variables.insert(index, variable)


    def remove_variable(self, variable):
        """Removes a :py:class:`.Variable` column from the Dataset.

        :param Variable variable: the Variable to remove."""

        self._variables.remove(variable)


    def pop_variable(self, index=-1):
        """Removes and returns the variable at a given index - by default the
        last one.

        :param int index: The index to remove at (default is ``-1``).
        :returns: the specified Variable."""

        return self._variables.pop(index)
