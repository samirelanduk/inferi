Overview
--------

inferi is a tool for performing basic statistical analysis on datasets. It is
pure-Python, and has no compiled dependencies.

Series
~~~~~~

The fundamental unit of inferi data analysis is the :py:class:`.Series`. It
represents a set of measurements, such as heights, or favourite colours.

    >>> import inferi
    >>> heights = inferi.Series(178, 156, 181, 175, 178)
    >>> heights
    '<Series: (178, 156, 181, 175, 178)>'
    >>> heights.length()
    5

If you like, you can give the series a name as an appropriate label:

    >>> heights = inferi.Series(178, 156, 181, 175, 178, name="heights")
    >>> heights.name()
    'heights'

Samples and Populations
#######################

While a series generally represents a set of measurements, the entities that
those measurements are made on (the 'experimental units') can either be an
entire population, or a subset of that population.

For example, if you measure the heights of all the children in a class, the
resulting series would be a population. If you ask a hundred people how many
people they have they have in their address book, that series is only a sample
because there are more than 100 people in the population you wish to learn
something about.

In inferi, this distinction is made with the :py:meth:`~.Series.sample`
property. The default is to assume the series is a sample:

    >>> heights = inferi.Series(178, 156, 181, 175, 178)
    >>> heights.sample()
    True
    >>> contact_counts = inferi.Series(34, 12, 19, 76, 44, sample=False)
    >>> heights.sample()
    False


Measures of centrality
######################

Series have the basic measures of centrality - mean, median and range.

    >>> heights = inferi.Series(178, 156, 181, 175, 178)
    >>> heights.mean()
    173.6
    >>> heights.median()
    178
    >>> heights.mode()
    178

See the full documentation for details on :py:meth:`~.Series.mean`,
:py:meth:`~.Series.median`, and :py:meth:`~.Series.mode`. Note that if the
series has more than one mode, ``None`` will be returned.

Measures of dispersion
######################

Series can also calculate various measures of dispersion, the simplest being
the range:

    >>> heights = inferi.Series(178, 156, 181, 175, 178)
    >>> heights.range()
    25

You can also calculate the variance and the standard deviation - measures of
how far individual measurements tend to be from the mean:

    >>> heights.variance()
    101.3
    >>> heights.standard_deviation()
    10.064790112068906

Again, see the full documentation of :py:meth:`~.Series.range`,
:py:meth:`~.Series.variance`, and :py:meth:`~.Series.standard_deviation` for
more details.
