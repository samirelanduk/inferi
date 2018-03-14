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



class Event:
    """An occurance that is made up of multiple simple events.

    :param \*simple_events: The :py:class:`.SimpleEvent` objects within this\
    set.
    :param str name: The name of the event (default is 'E').
    :raises TypeError: if non-simple-events are given.
    :raises TypeError: if the name is not a string."""

    def __init__(self, *simple_events, name="E"):
        if any(not isinstance(e, SimpleEvent) for e in simple_events):
            raise TypeError(f"Event needs SimpleEvents: {simple_events}")
        if not isinstance(name, str):
            raise TypeError(f"Name {name} is not str")
        self._simple_events = set(simple_events)
        self._name = name


    def __repr__(self):
        return f"<Event '{self._name}'>"


    def simple_events(self):
        """The set of simple events in this event.

        :rtype: ``set``"""

        return set(self._simple_events)


    def name(self):
        """Returns the name of the Event.

        :rtype: ``str``"""

        return self._name


    def probability(self):
        """Returns the probability of the event happening.

        :rtype: ``float``"""

        return sum(e.probability() for e in self._simple_events)



class SampleSpace:
    """The set of all possible things that can result from a statistical
    experiment.

    :param \*outcomes: All the possible outcomes.
    :param dict p: The probabilities for the supplied outcomes. If not given,\
    these will be weighted equally.
    :raises ValueError: if you supply probabilities that don't add up to 1."""

    def __init__(self, *outcomes, p=None):
        if not outcomes and not p:
            raise ValueError("Sample spaces need at least one outcome")
        if p is None:
            p_per_event = 1 / len(outcomes)
            p = {event: p_per_event for event in outcomes}
        else:
            unaccounted_events = [e for e in outcomes if e not in p]
            if unaccounted_events:
                p_per_event = (1 - sum(p.values())) / len(unaccounted_events)
                for e in unaccounted_events:
                    p[e] = p_per_event
        if round(sum(p.values()), 8) != 1:
            raise ValueError("Probabilities do not add up to 1: {}".format(p))
        self._simple_events = set([SimpleEvent(e, p[e]) for e in p])


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


    def outcomes(self, p=False):
        """The set of outcomes that the sample space's simple events can
        produce.

        :rtype: ``set``"""

        if p: return {e.outcome(): e.probability() for e in self._simple_events}
        return set([e.outcome() for e in self._simple_events])


    def event(self, *outcomes, name=None):
        """Returns the :py:class:`.SimpleEvent` corresponding to the outcome\
        given (or ``None`` if there is no such simple event).

        :param outcome: The outcome to look for.
        :rtype: ``SimpleEvent``"""

        if len(outcomes) == 1:
            for event in self._simple_events:
                if event.outcome() == outcomes[0]:
                    return event
        else:
            simple = [e for e in self._simple_events if e.outcome() in outcomes]
            return Event(*simple, name=name) if name else Event(*simple)


    def chances_of(self, outcome):
        """Returns the probability of the given outcome occuring in a single
        statistical experiment.

        :param outcome: The outcome to test for."""

        event = self.event(outcome)
        return event.probability() if event is not None else 0


    def experiment(self):
        """Generate an outcome."""

        outcomes = self.outcomes(p=True)
        outcomes = [(o, p) for o, p in outcomes.items()]
        outcomes, odds = zip(*outcomes)
        return random.choices(outcomes, weights=odds, k=1)[0]
