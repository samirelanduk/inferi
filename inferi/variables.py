class Variable(list):

    def __init__(self, *args, **kwargs):
        list.__init__(self, [*args], **kwargs)
