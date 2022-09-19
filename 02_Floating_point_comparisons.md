## Floating point comparisons

[`numpy.isclose`]: https://numpy.org/doc/stable/reference/generated/numpy.isclose.html
[`numpy.allclose`]: https://numpy.org/doc/stable/reference/generated/numpy.allclose.html
[`numpy.nan`]: https://numpy.org/doc/stable/reference/constants.html#numpy.nan

[`astropy.units.Quantity`]: https://docs.astropy.org/en/stable/api/astropy.units.Quantity.html
[`astropy.units.isclose`]: https://docs.astropy.org/en/stable/api/astropy.units.isclose.html
[`astropy.units.allclose`]: https://docs.astropy.org/en/stable/api/astropy.units.allclose.html

[`assert_quantity_allclose`]: https://docs.astropy.org/en/latest/api/astropy.tests.helper.assert_quantity_allclose.html

Floating point comparisons are fraught with peril, in particular if we
do comparisons with the `==` operator.

```pycon
>>> assert 0.1 + 0.2 == 0.3
False
```

The issue is that there is a very slight difference at the level of
machine precision.  

```pycon
>>> 0.1 + 0.2 - 0.3
5.551115123125783e-17
```

We can use [`numpy.isclose`] when we are trying to compare floating
point numbers that might be slightly different.

```pycon
>>> import numpy as np
>>> np.isclose(0.1 + 0.2, 0.3)
True
>>> assert np.isclose(0.1 + 0.2, 0.3)
```

We can also specify how close the numbers have to be to each other using
the `atol` and `rtol` keywords.  The `atol` keyword specifies the
absolute tolerance, i.e. the maximum allowed absolute difference between
the two values for them to compare as "close." The following line
returns `True` because `10.0` and `11.0` have an  absolute  difference
of ≤ 1.  


```pycon
>>> np.isclose(10.0, 11.0, atol=1)
True
```

If we switch it to `atol=0.99`, it becomes `False`.

```pycon
>>> np.isclose(10.0, 11.0, atol=0.99)
False
```

Similarly, we can specify the relative difference between the two 
numbers using the `rtol` keyword.

```pycon
>>> np.isclose(10.0, 11.0, rtol=0.1)
True
>>> np.isclose(10.0, 11.0, rtol=0.09)
False
```

The docstring for [`numpy.isclose`] specifies the defaults for `atol`
and `rtol`. When we compare numbers with magnitudes that are 𝒪(1), the
default values for `atol` and `rtol` are typically fine. When we compare
numbers with magnitudes that are ≪1 or ≫1, then we want to specify the
numbers more carefully.  

To compare lists and arrays, we can use [`numpy.allclose`].

```pycon
>>> ones = np.ones(5)
>>> twos = 2 * ones
>>> assert np.allclose(ones, twos)
False
```

### Comparisons between `Quantity` objects

We can also use [`astropy.units.isclose`] and [`astropy.units.allclose`]
in order to compare [`astropy.units.Quantity`] objects.

```pycon
>>> import astropy.units as u
>>> u.isclose(5 * u.kg, 6 * u.kg)
False
>>> assert u.allclose([5, 6] * u.m, [5, 6] * u.m)
True
```

We can also use [`assert_quantity_allclose`].

```pycon
>>> from astropy.tests.helper import assert_quantity_allclose
>>> assert_quantity_allclose([1, 2] * u.m, [1.2 , 2] * u.m)
```

### Comparing NaN values

[`numpy.nan`] is a floating point representation of "Not a Number." Many
of the functions we write may encounter [`numpy.nan`] values from time
to time and should be tested. We should be careful though, because
[`numpy.nan`] is not equal to itself.

```pycon
>>> np.nan == np.nan
False
```

What's happening here is that NumPy is following the [IEEE 754] standard
for floating point math.  We can use [`numpy.isclose`] for this too, as
long as we set the `equal_nan` keyword to `True`.

```pycon
>>> np.isclose(np.nan, np.nan)
False
>>> np.isclose(np.nan, np.nan, equal_nan=True)
True
```
