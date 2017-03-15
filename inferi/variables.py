class Variable(list):

    def __init__(self, *args, name=None, **kwargs):
        list.__init__(self, [*args], **kwargs)

        if not isinstance(name, str) and name is not None:
            raise TypeError("Variable name must be str, not '%s'" % str(name))
        self._name = name


    def __repr__(self):
        if self._name:
            return "<'%s': %s>" % (self._name, list.__repr__(self))
        else:
            return "<Variable: %s>" % list.__repr__(self)
