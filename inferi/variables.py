class Variable(list):

    def __init__(self, *args, name=None, **kwargs):
        list.__init__(self, [*args], **kwargs)

        if not isinstance(name, str) and name is not None:
            raise TypeError("Variable name must be str, not '%s'" % str(name))
        self._name = name
