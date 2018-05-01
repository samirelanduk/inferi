Overview
--------

inferi is a tool for performing basic statistical analysis on datasets. It is
pure-Python, and has no compiled dependencies.

Variables
~~~~~~~~~

The fundamental unit of inferi data analysis is the :py:class:`.Variable`. It
represents a set of measurements, such as heights, or favourite colours. It is
`not` the same as a Python variable - it represents variables in the statistics
sense of the word.

    >>> import inferi
    >>> heights = inferi.Variable(178, 156, 181, 175, 178)
    >>> heights
    '<Variable (178, 156, 181, 175, 178)>'
    >>> heights.length
    5

If you like, you can give the variable a name as an appropriate label:

    >>> heights = inferi.Variable(178, 156, 181, 175, 178, name="heights")
    >>> heights.name
    'heights'

You can also give an existing sequence, such as a list, and the result will be
the same:

  >>> heights = inferi.Variable([178, 156, 181, 175, 178])
  >>> heights
  '<Variable (178, 156, 181, 175, 178)>'

Values can be accessed by indexing:

  >>> weights.values
  (12, 19, 11)
  >>> weights[0]
  12
  >>> weights[-1]
  11
  >>> weights.max
  19
  >>> weights.min
  11

Measures of Centrality
######################

Variables have the basic measures of centrality - mean, median and range.

    >>> heights = inferi.Variable(178, 156, 181, 175, 178)
    >>> heights.mean
    173.6
    >>> heights.median
    178
    >>> heights.mode(
    178

See the full documentation for details on :py:attr:`~.Variable.mean`,
:py:attr:`~.Variable.median`, and :py:attr:`~.Variable.mode`. Note that if the
variable has more than one mode, ``None`` will be returned.


Measures of Dispersion
######################

Variables can also calculate various measures of dispersion, the simplest being
the range:

    >>> heights = inferi.Variable(178, 156, 181, 175, 178)
    >>> heights.range
    25

You can also calculate the variance and the standard deviation - measures of
how far individual measurements tend to be from the mean:

    >>> heights.variance()
    101.3
    >>> heights.st_dev()
    10.064790112068906

By default the Variables will be treated as samples rather than populations,
which has consequences on the value of both the variance and the standard
deviation. To get the population values for each, simply set this when you
call the method:

  >>> heights.variance(population=True)
  81.04
  >>> heights.st_dev(population=True)
  9.00222194794152

Again, see the full documentation of :py:attr:`~.Variable.range`,
:py:meth:`~.Variable.variance`, and :py:meth:`~.Variable.st_dev` for
more details.


Comparing Variables
###################

It is often useful to compare how two variables are related - whether there is a
correlation between them or if they are independent.

A simple way of doing this is to find the covariance between them, using the
:py:meth:`~.Variable.covariance_with` method:

    >>> variable1 = inferi.Variable(2.1, 2.5, 4.0, 3.6)
    >>> variable2 = inferi.Variable(8, 12, 14, 10)
    >>> variable1.covariance_with(variable2)
    0.8033333333333333

The sign of this value tells you the relationship - if it is positive they are
positively correlated, negative and they are negatively correlated, and the
closer to zero it is, the more independent the variable are.

However the actual value of the covariance doesn't tell you much because it
depends on the magnitude of the values in the variable. The correlation metric
however, is normalised to be between -1 and 1, so it is easier to quantify how
related the two variable are. :py:meth:`~.Variable.correlation_with` is used to
calculate this:

    >>> variable1 = inferi.Variable(2.1, 2.5, 4.0, 3.6)
    >>> variable2 = inferi.Variable(8, 12, 14, 10)
    >>> variable1.correlation_with(variable2)
    0.662573882203029

Datasets
~~~~~~~~

Usually, more than one thing is measured in an experiment, and so you would have
more than one variable. For example, you might ask someone's name, their age,
their height, and whether or not they smoke. Each of these four metrics is a
variable:

  >>> variable1 = inferi.Variable("Jon", "Sue", "Bob", name="Names")
  >>> variable2 = inferi.Variable(19, 34, 38, name="Ages")
  >>> variable3 = inferi.Variable(1.87, 1.67, 1.73, name="Heights")
  >>> variable4 = inferi.Variable(False, True, True, name="Smokes")

These can be combined into a single :py:class:`.Dataset` as follows:

  >>> dataset = inferi.Dataset(variable1, variable2, variable3, variable4)
  >>> dataset.variables
  (<Variable 'Names' ('Jon', 'Sue', 'Bob')>, <Variable 'Ages' (19, 34, 38)>, <Va
  riable 'Heights' (1.87, 1.67, 1.73)>, <Variable 'Smokes' (False, True, True)>)

A dataset can be thought of as representing a table of data, where each variable
is a column. This dataset represents a table like this::

    Names Ages Heights Smokes

    Jon   19   1.87    No
    Sue   34   1.67    Yes
    Bob   38   1.73    Yes

You can get the rows of a dataset too:

  >>> dataset.rows
  (('Jon', 19, 1.87, False), ('Sue', 34, 1.67, True), ('Bob', 38, 1.73, True))

A Dataset can be sorted, by default by the first column but this can be made
otherwise:

  >>> dataset.sort()
  >>> datset.rows
  (('Bob', 38, 1.73, True), ('Jon', 19, 1.87, False), ('Sue', 34, 1.67, True))
  >>> dataset.sort(variable3)
  >>> dataset.rows
  (('Sue', 34, 1.67, True), ('Bob', 38, 1.73, True), ('Jon', 19, 1.87, False))

Probability
~~~~~~~~~~~

Probabilty is a way of looking all the ways something *can* happen and assessing
how likely the outcomes are.

Everyone's favourite example is rolling a die - there are six possible outcomes
in the Sample Space:

  >>> space = inferi.SampleSpace(1, 2, 3, 4, 5, 6)

This defines a sample space with six outcomes. Each of these is a simple event:

  >>> space.simple_events
  {<SimpleEvent: 1>, <SimpleEvent: 2>, <SimpleEvent: 3>, <SimpleEvent: 4>, <Simp
  leEvent: 5>, <SimpleEvent: 6>}
  >>> space.event(5)
  <SimpleEvent: 5>
  >>> space.event(5).probability()
  0.16666666666666666
  >>> space.event(5).probability(fraction=True)
  Fraction(1, 6)
  >>> space.chances_of(5)
  0.16666666666666666

Events are some combination of simple events. For example, to define the event
that a rolled die produces an even number:

  >>> even_event = space.event(lambda o: o % 2 == 0, name="even")
  >>> even_event
  <Event: even>
  >>> even_event.name
  'even'
  >>> even_event.probability()
  0.5
  >>> even_event.outcomes()
  {2, 4, 6}
  >>> even_event.outcomes(p=True)
  {2: 0.16666666666666666, 4: 0.16666666666666666, 6: 0.16666666666666666}
  >>> even_event in space
  True

Two events can be compared. Here we create two more events:

  >>> odd_event = space.event(lambda o: o % 2 != 0, name="odd")
  >>> large_event = space.event(lambda o: o > 4)
  >>> odd_event.mutually_exclusive_with(even_event)
  True
  >>> large_event.mutually_exclusive_with(even_event)
  False
  # Does knowing number is even affect chances of being odd? (Obviously...)
  >>> odd_event.dependent_on(even_event)
  True
  # Does knowing number is even affect chances of being greater than 4?
  >>> large_event.dependent_on(even_event)
  False

You can even make new events from them...

  >>> small_and_even = large_event.complement & even_event
  >>> small_and_even.probability()
  0.333333333333333
  >>> small_and_even.outcomes()
  {2, 4}
