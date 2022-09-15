## Floating point comparisons

Floating point comparisons are fraught with peril!

```pycon
>>> assert 0.1 + 0.2 == 0.3
False

>>> 0.1 + 0.2 - 0.3
5.551115123125783e-17
```

We need to use `numpy.isclose`.

```pycon
>>> import numpy as np
>>> np.isclose(0.1 + 0.2, 0.3)
True
>>> assert np.isclose(0.1 + 0.2, 0.3)
```

We can also specify a relative tolerance with `rtol` and an absolute
tolerance with `atol`.

```pycon
>>> np.isclose(0.5, 5.0001, rtol=1e-4)
False
>>> np.isclose(1, 1.0001, atol=1e-3)
True
```

To compare lists and arrays, we can use `np.allclose`.

```pycon
>>> ones = np.ones(5)
>>> twos = 2 * ones
>>> assert np.allclose(ones, twos)
False
```

We can also use `isclose` and `allclose` from `astropy.units`.

```pycon
>>> import astropy.units as u
>>> u.isclose(5 * u.kg, 6 * u.kg)
False
>>> assert u.allclose([5, 6] * u.m, [5, 6] * u.m)
True
```

But we have to be careful!

```pycon
>>> np.nan == np.nan
False
>>> np.inf == np.inf
False
```

What's happening here is that NumPy is following rules for the IEEE
standard for floating point math.  We can use `numpy.isclose` for this
too.
```pycon
>>> np.isclose(np.nan, np.nan)
False
>>> np.isclose(np.nan, np.nan, equal_nan=True)
True
```