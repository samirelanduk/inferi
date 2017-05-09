"""Contains the Sample class."""

from .datasets import Dataset

class Sample(Dataset):
    """Base class: :py:class:`.Dataset`

    A Sample is a dataset of discrete experimental units with no particular
    order. Each experimental unit of the sample has a measurement associated
    with it.

    For example, the heights of children in a classroom could be represented as
    a sample.

    :param \*rows: The measurements that make up the Sample."""

    def __init__(self, *args, **kwargs):
        Dataset.__init__(self, *args, **kwargs)


    def __repr__(self):
        return "<Sample {}>".format(tuple(self._data.values()))
