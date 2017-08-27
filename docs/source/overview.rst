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
    >>> heights.length()
    5

If you like, you can give the variable a name as an appropriate label:

    >>> heights = inferi.Variable(178, 156, 181, 175, 178, name="heights")
    >>> heights.name()
    'heights'

You can also give an existing sequence, such as a list, and the result will be
the same:

  >>> heights = inferi.Variable([178, 156, 181, 175, 178])
  >>> heights
  '<Variable (178, 156, 181, 175, 178)>'

Finally, you can choose to provide error values for the values in the
Variable, like so:

  >>> weights = inferi.Variable(12, 19, 11, error=[0.9, 1.1, 0.7])

You must provide an equal number of error values as regular values.

Values can be accessed by indexing or with :py:meth:`~.Variable.get`:

  >>> weights.values()
  (12, 19, 11)
  >>> weights.error()
  (0.9, 1.1, 0.7)
  >>> weights[0]
  12
  >>> weights[-1]
  11
  >>> weights.get(1)
  19
  >>> weights.get(1, error=True)
  19 ± 1.1
  >>> weights.max()
  19
  >>> weights.min(error=True)
  11 ± 0.7

Many Variable methods which return a value can be given ``error=True`` and the
result will be returned as a `fuzz <https://fuzz.samireland.com/>`_ ``Value``
object, with error built in.

Measures of Centrality
######################

Variables have the basic measures of centrality - mean, median and range.

    >>> heights = inferi.Variable(178, 156, 181, 175, 178)
    >>> heights.mean()
    173.6
    >>> heights.median()
    178
    >>> heights.mode()
    178

See the full documentation for details on :py:meth:`~.Variable.mean`,
:py:meth:`~.Variable.median`, and :py:meth:`~.Variable.mode`. Note that if the
variable has more than one mode, ``None`` will be returned.


Measures of Dispersion
######################

Variables can also calculate various measures of dispersion, the simplest being
the range:

    >>> heights = inferi.Variable(178, 156, 181, 175, 178)
    >>> heights.range()
    25

You can also calculate the variance and the standard deviation - measures of
how far individual measurements tend to be from the mean:

    >>> heights.variance()
    101.3
    >>> heights.st_dev()
    10.064790112068906

By default the Variables will be treated as samples rather than populations,
which has consequences on the valye of both the variance and the standard
deviation. To get the population values for each, simply set this when you
call the method:

  >>> heights.variance()
  81.04
  >>> heights.st_dev()
  9.00222194794152

Again, see the full documentation of :py:meth:`~.Variable.range`,
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


Combining Variables
###################

Variables can be added, subtracted, and averaged:

  >>> variable1 = inferi.Variable(2.1, 2.5, 4.0, 3.6)
  >>> variable2 = inferi.Variable(8, 12, 14, 10)
  >>> variable1 + variable2
  <Variable (10.1, 14.5, 18.0, 13.6)>
  >>> variable2 - variable1
  <Variable (5.9, 9.5, 10.0, 6.4)>
  >>> inferi.Variable.average(variable1, variable2)
  <Variable (5.05, 7.25, 9.0, 6.8)>

Error values will be retained and combined appropriately across all operations.
See the `fuzz <https://fuzz.samireland.com/>`_ for details on how this is done.
