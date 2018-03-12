from math import factorial
import itertools

def permutations(n, r=None):
    """Returns the number of ways of arranging r elements of a set of size n in
    a given order - the number of permuatations.

    :param int n: The size of the set containing the elements.
    :param int r: The number of elements to arange. If not given, it will be\
    assumed to be equal to n.
    :raises TypeError: if non-integers are given.
    :raises ValueError: if r is greater than n.
    :rtype: ``int``"""

    if not isinstance(n, int): raise TypeError("n {} must be integer".format(n))
    if r is None: return factorial(n)
    if not isinstance(r, int): raise TypeError("r {} must be integer".format(r))
    if r > n:
        raise ValueError("r {} is larger than n {}".format(r, n))
    return factorial(n) / factorial(n - r)


def combinations(n, r=None):
    """Returns the number of ways of combining r elements of a set of size n,
    where order doesn't matter

    :param int n: The size of the set containing the elements.
    :param int r: The number of elements to arange. If not given, it will be\
    assumed to be equal to n.
    :raises TypeError: if non-integers are given.
    :raises ValueError: if r is greater than n.
    :rtype: ``int``"""

    if not isinstance(n, int): raise TypeError("n {} must be integer".format(n))
    r = n if r is None else r
    if not isinstance(r, int): raise TypeError("r {} must be integer".format(r))
    if r > n:
        raise ValueError("r {} is larger than n {}".format(r, n))
    return factorial(n) / (factorial(r) * factorial(n - r))


def permutate(collection, r=None):
    """Generates all the permutations of a given iterable, of a given length.

    It is essentially a wrapper around the built-in ``itertools.permutations``.

    :param iterable collection: The iterable to permutate.
    :param int r: The number of elements to arange. If not given, it will be\
    assumed to be equal to the length of the collection.
    :raises ValueError: if r is greater than the length of the collection.
    :rtype: ``tuple``"""

    n = len(tuple(collection))
    if r is not None and r > n:
        raise ValueError("r {} is larger than n {}".format(r, n))
    return itertools.permutations(collection, r=r)


def combine(collection, r=None):
    """Generates all the combinations of a given iterable, of a given length.

    It is essentially a wrapper around the built-in ``itertools.combinations``.

    :param iterable collection: The iterable to combine.
    :param int r: The number of elements to arange. If not given, it will be\
    assumed to be equal to the length of the collection.
    :raises ValueError: if r is greater than the length of the collection.
    :rtype: ``set``"""

    n = len(tuple(collection))
    if r is not None and r > n:
        raise ValueError("r {} is larger than n {}".format(r, n))
    r = n if r is None else r
    for combination in itertools.combinations(collection, r=r):
        yield set(combination)
