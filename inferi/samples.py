"""Contains the Sample class."""

from .datasets import Dataset

class Sample(Dataset):

    def __init__(self, *args, **kwargs):
        Dataset.__init__(self, *args, **kwargs)
