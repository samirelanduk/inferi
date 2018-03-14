import random

class SimpleEvent:
    """A simple event - a single outcome of a statistical experiment.

    :param outcome: The result of this event occuring.
    :param float probability: The probability of this event occuring.
    :raises TypeError: if probability isn't numeric.
    :raises ValueError: if probability is not between 0 and 1."""

    def __init__(self, outcome, probability):
        self._outcome = outcome
        if not isinstance(probability, (int, float)):
            raise TypeError("probability {} is not numeric".format(probability))
        if not 0 <= probability <= 1:
            raise ValueError("probability {} is invalid".format(probability))
        self._probability = probability


    def __repr__(self):
        return "<SimpleEvent: {}>".format(self._outcome)


    def outcome(self):
        """The result of this event occuring."""

        return self._outcome


    def probability(self):
        """The probability of this event occuring."""

        return self._probability



class SampleSpace:
    """The set of all possible things that can result from a statistical
    experiment.

    :param \*simple_events: All the possible outcomes."""

    def __init__(self, *simple_events):
        p = 1 / len(simple_events)
        self._simple_events = set([SimpleEvent(e, p) for e in simple_events])


    def __repr__(self):
        return "<SampleSpace ({} simple events)>".format(
         len(self._simple_events)
        )


    def __contains__(self, item):
        return item in self._simple_events or item in self.outcomes()


    def simple_events(self):
        """The set of simple events in this sample space.

        :rtype: ``set``"""

        return set(self._simple_events)


    def outcomes(self):
        """The set of outcomes that the sample space's simple events can
        produce.

        :rtype: ``set``"""

        return set([e.outcome() for e in self._simple_events])


    def event(self, outcome):
        """Returns the :py:class:`.SimpleEvent` corresponding to the outcome\
        given (or ``None`` if there is no such simple event).

        :param outcome: The outcome to look for.
        :rtype: ``SimpleEvent``"""

        for event in self._simple_events:
            if event.outcome() == outcome:
                return event


    def chances_of(self, outcome):
        """Returns the probability of the given outcome occuring in a single
        statistical experiment.

        :param outcome: The outcome to test for."""

        event = self.event(outcome)
        return event.probability() if event is not None else 0


    def experiment(self):
        """Generate an outcome."""

        return random.sample(self.outcomes(), 1)[0]
