import random

class Event:
    """An occurance that is made up of multiple simple events.

    Events are containers both of their simple events, and the outcomes of those
    simple events.

    :param \*events: The :py:class:`.Event` objects within this set.
    :param str name: The name of the event (default is 'E').
    :raises TypeError: if non-events are given.
    :raises TypeError: if the name is not a string."""

    def __init__(self, *events, name="E"):
        if any(not isinstance(e, Event) for e in events):
            raise TypeError(f"{events} contains non-events")
        if not isinstance(name, str):
            raise TypeError(f"Name {name} is not str")
        self._simple_events = set()
        for event in events: self._simple_events.update(event._simple_events)
        self._name = name


    def __repr__(self):
        return f"<{self.__class__.__name__}: {self._name}>"


    def __contains__(self, member):
        if isinstance(member, Event):
            return member._simple_events.issubset(self._simple_events)
        for event in self._simple_events:
            if event._outcome == member: return True


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

        return sum(event._probability for event in self._simple_events)


    def mutually_exclusive_with(self, event):
        """Looks at some other event and checks if this event is mutually
        exclusive with the other event. That is, whether it is impossible for
        them both to happen in a given statistical experiment.

        :param Event event: the other event to check with.
        :raises TypeError: if a non-Event is given.
        :rtype: ``bool``"""

        if not isinstance(event, Event):
            raise TypeError(f"{event} is not an event")
        return not self._simple_events & event._simple_events



class SimpleEvent(Event):
    """Base class: py:class:`.Event`

    A simple event - a single outcome of a statistical experiment.

    :param outcome: The result of this event occuring.
    :param float probability: The probability of this event occuring.
    :raises TypeError: if probability isn't numeric.
    :raises ValueError: if probability is not between 0 and 1."""

    def __init__(self, outcome, probability):
        self._outcome = self._name = outcome
        if not isinstance(probability, (int, float)):
            raise TypeError("probability {} is not numeric".format(probability))
        if not 0 <= probability <= 1:
            raise ValueError("probability {} is invalid".format(probability))
        self._probability = probability
        self._simple_events = set((self,))


    def outcome(self):
        """The result of this event occuring."""

        return self._outcome



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
            raise ValueError(f"Probabilities do not add up to 1: {p}")
        self._simple_events = set([SimpleEvent(e, p[e]) for e in p])


    def __repr__(self):
        return f"<SampleSpace ({len(self._simple_events)} simple events)>"


    def __contains__(self, item):
        for event in self._simple_events:
            if item is event or item == event.outcome(): return True
        if isinstance(item, Event):
            return event._simple_events.issubset(self._simple_events)


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
        """If a single outcome is given, this function will return the
        :py:class:`.SimpleEvent` corresponding to that outcome.

        If multiple outcomes are given, the function will return the
        :py:class:`.Event` corresponding to one of those outcomes occuring.

        If a callable is provided, the function will return the
        :py:class:`.Event` of all the simple events that return ``True`` when
        the callable is applied to their outcome.

        :param \*outcomes: The outcome(s) to look for.
        :param str name: The name to apply if a :py:class:`.Event` is returned.
        :rtype: ``SimpleEvent`` or ``Event``"""

        if len(outcomes) == 1:
            if callable(outcomes[0]):
                f = outcomes[0]
                outcomes = [
                 e.outcome() for e in self._simple_events if f(e.outcome())
                ]
            else:
                for event in self._simple_events:
                    if event.outcome() == outcomes[0]: return event
                else: return None
        simple = [e for e in self._simple_events if e.outcome() in outcomes]
        return Event(*simple, name=name) if name else Event(*simple)


    def chances_of(self, *outcomes):
        """Returns the probability of the given outcome or outcomes occuring in
        a single statistical experiment.

        If multiple outcomes are given, the function will return the
        :py:class:`.Event` corresponding to one of those outcomes occuring.

        If a callable is provided, the function will return the
        :py:class:`.Event` of all the simple events that return ``True`` when
        the callable is applied to their outcome.

        :param \*outcomes: The outcome(s) to look for.
        :rtype: ``float``"""

        event = self.event(*outcomes)
        return event.probability() if event is not None else 0


    def experiment(self):
        """Generate an outcome."""

        outcomes = self.outcomes(p=True)
        outcomes = [(o, p) for o, p in outcomes.items()]
        outcomes, odds = zip(*outcomes)
        return random.choices(outcomes, weights=odds, k=1)[0]
