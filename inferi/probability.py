import random

class SimpleEvent:
    """A simple event - a single outcome of a statistical experiment.

    :param outcome: The result of this event occuring."""

    def __init__(self, outcome):
        self._outcome = outcome


    def __repr__(self):
        return "<SimpleEvent: {}>".format(self._outcome)


    def outcome(self):
        """The result of this event occuring."""

        return self._outcome



class SampleSpace:
    """The set of all possible things that can result from a statistical
    experiment.

    :param \*simple_events: All the possible outcomes."""

    def __init__(self, *simple_events):
        self._simple_events = set([SimpleEvent(e) for e in simple_events])


    def __repr__(self):
        return "<SampleSpace ({} simple events)>".format(
         len(self._simple_events)
        )


    def simple_events(self):
        """The set of simple events in this sample space.

        :rtype: ``set``"""

        return set(self._simple_events)


    def outcomes(self):
        """The set of outcomes that the sample space's simple events can
        produce.

        :rtype: ``set``"""
        
        return set([e.outcome() for e in self._simple_events])
