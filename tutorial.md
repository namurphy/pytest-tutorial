# pytest tutorial

To get ready for this tutorial, please follow these instructions to [install `uv`].
We won't use `uv` much, but it'll make a few things a lot easier.

[install `uv`]: https://docs.astral.sh/uv/getting-started/installation

## Getting set up

Let's create a directory to work in.

```bash
mkdir crane_pytest
cd crane_pytest
```

Let's create a virtual environment:

```bash
uv venv
```

This command will print out a command to activate this environment.
For Linux, this will be:

```bash
source .venv/bin/activate  # works on Linux; will differ for macOS & Windows
```

Then let's install some packages:

```bash
uv pip install pytest numpy
```

> [!TIP]
> Comments in a Unix terminal begin with `#`.

Let's start from within Python! (If you'd prefer, you can use a Jupyter notebook.)

```bash
python
```

## Assertions

An `assert` statement allows us to check whether a particular condition
is true. If we `assert` something true, then nothing happens.

```pycon
>>> assert True
```

If we assert something false, then we get an `AssertionError`.

```pycon
>>> assert False
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AssertionError
```

<!--
We can use `assert` statements in a few ways. We could put them directly
into code that we write in order to make sure that a particular
condition is true. We can also use `assert` statements to test software.
-->

We can use `assert` to test whether two or more objects
are equal (or unequal) to each other.

```pycon
>>> assert 1 == 2
False
>>> assert 1 != 2
True
```

Let's create a failing test.

```pycon
>>> assert 6 * 9 == 42
```

We can also add an error message for when the assertion is false.

```pycon
>>> assert [1, 2] == [3, 4], "List contents are not equal."
```

## Truthiness in Python

We can use `bool()` to tell whether Python considers something truthy
or falsey.

```pycon
>>> bool(1)
True
>>> bool(0)
False
>>> bool("non-empty string")
True
>>> bool("")
False
```

> [!IMPORTANT]
> Empty collections are considered falsey,
> while non-empty collections are considered truthy.

Let's try empty and non-empty lists (created using square brackets).

```pycon
>>> bool( [] )
False
>>> bool( [1, 2, 3] )
True
```

## Exceptions

An exception is an error that happens when Python code is being executed.
An example is a `ZeroDivisionError`.

```pycon
>>> 1 / 0
```

We can raise our own exceptions,

```pycon
>>> raise ValueError
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError
```

and include error messages.

```pycon
>>> raise ValueError("We can add error messages here too!")
```

<!--
We can also handle exceptions with `try` 

```pycon
>>> x = 1
>>> y = 0
>>> try:
...     x / y
... except ZeroDivisionError:
...     print("Attempting to divide by zero.")
... else:  # will run if there is no exception
...     print("Not attempting to divide by zero.")
... finally:  # will always run
...     print("All done!")
Attempting to divide by zero.
```
-->

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
```

The problem is that there is a very slight difference at the level of
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

The `atol` keyword to `numpy.isclose` specifies the
**absolute tolerance**, i.e. the maximum allowed absolute difference between
two values for them to compare as "close."

The following line returns `True` because `10.0` and `11.0` have an
absolute  difference of ≤ 1.

```pycon
>>> np.isclose(10.0, 11.0, atol=1.01)
True
```

If we switch it to `atol=0.99`, it becomes `False`.

```pycon
>>> np.isclose(10.0, 11.0, atol=0.99)
False
```

Similarly, we can specify the **relative tolerance** between the two
numbers using the `rtol` keyword.

```pycon
>>> np.isclose(10.0, 11.0, rtol=0.1)
True
>>> np.isclose(10.0, 11.0, rtol=0.09)
False
```

> [!IMPORTANT]
> The docstring for [`numpy.isclose`] specifies the defaults for `atol`
> and `rtol`. When we compare numbers with magnitudes that are significantly
> larger or smaller than one, we will need to specify numbers more carefully.

To compare lists and arrays, we can use [`numpy.allclose`].

```pycon
>>> ones = np.ones(5)
>>> twos = 2 * ones
>>> assert np.allclose(ones, twos)
False
```
> [!TIP]
> We can also use [`astropy.units.isclose`] and [`astropy.units.allclose`]
> in order to compare [`astropy.units.Quantity`] objects with units.

<!--
### Comparisons between `Quantity` objects


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
-->


<!--
### Comparing NaN values

[`numpy.nan`] is an object that represents "not a number."

```pycon
>>> zeros = numpy.zeros(4)
>>> print(zeros)
>>> zeros / zeros
```



Many
of the functions we write may encounter `numpy.nan` values. We should be careful though, because
`numpy.nan` is not equal to itself.

```pycon
>>> np.nan == np.nan
False
```
-->

<!--
What's happening here is that NumPy is following the [IEEE 754] standard
for floating point math.
-->
<!--
We can use [`numpy.isclose`] for this too if we set the `equal_nan` keyword to `True`.

We can use [`numpy.isclose`] for this too, as
long as we set the `equal_nan` keyword to `True`.

```pycon
>>> np.isclose(np.nan, np.nan)
False
>>> np.isclose(np.nan, np.nan, equal_nan=True)
True
```
-->


Now let's exit Python.

```pycon
>>> exit
```

## Let's write a software test

Let's make sure `pytest` is installed.

```bash
pytest --version
```

Let's initialize a Python project.

```bash
uv init double
```

Let's enter the directory and see what's in it.
If using PowerShell, use `dir` instead of `ls -A`.

```bash
cd double
ls -A  # use dir in PowerShell
```

Let's open `main.py` with your favorite plain text editor.  
I'll use `nano` since it is a common text editor in a terminal.

```bash
nano main.py
```

At the top of `main.py`, let's define a function called `double()`.

```python
def double(x):
    return 2 * x
```

Save the file and exit. (If using `nano`, press ctrl-x to exit, followed
by `y` and enter to save.)

Now let's create a file called `test_double.py`.

```bash
nano test_double.py
```

> [!NOTE]
> The name of the file must begin with `test_` so that `pytest` knows
> that it contains tests.

In `test_double.py`, let's create a function called `test_doubling_one()`.

```python
import main


def test_doubling_one():
    assert double(1) == 2 
```

> [!NOTE]
> The name of each test must also begin with `test_` so that `pytest`
> treats it as a test.

Back in the terminal, let's run `pytest`.

```bash
pytest
```

In the output next to `test_double.py`, there should be a `.` which 
indicates that a test was run and it passed.

Let's see what happens when we add a test that fails. 

```python
def test_that_fails():
    assert double(1) == 347598234789433547903497
```

Let's run `pytest` again.

```bash
pytest
```

The `.F` indicates that the first test passed and the second test failed,
as intended. Let's take a look at the error message. 

The first line says that in `test_double.py`, on line ∼8, there is a 
test called `test_that_fails` which failed.
```
test_double.py:8: in test_that_fails
````

The next lines show what the left and right sides of the `assert`
statement evaluated to, step-by-step (i.e., that `main.double(1)`
evaluated to `2`).

```
    assert main.double(1) == 23790530
E   assert 2 == 23790530
```

The last two lines include the _memory address_ of `main.double()`, which
indicates where the function was stored in memory.
Memory address information usually doesn't matter, but can be helpful 
if we're working with `lambda` functions like `double = lambda x: 2 * x`.

```
E    +  where 2 = <function double at 0x7f04c551ad40>(1)
E    +    where <function double at 0x7f04c551ad40> = main.double
```



## Command line options

### Getting help

To see what command line options are available for pytest, run:

```bash
pytest --help
```

There are a lot! We'll cover a few of the options that we'll be more
likely to use.

### Running only the tests that failed last time

If we have a bunch of tests or tests that take a long time to run, we 
can use the ``--last-failed`` option which will run only the tests that
failed the last time that we ran the tests.  (If no tests failed, it
will run all the tests.)

```bash
$ pytest --last-failed
```

### Choosing which tests to run

We can use the `-k` flag for pytest to specify which tests we want run
based on which substrings appear.  If we do:

```bash
$ pytest -k one
```

then only `test_doubling_one` will be run because it's the only test
that has `one` in its name. If we do:

```bash
$ pytest -k two
```

then we'll similarly run only the tests that have `two` in their name.

### Shortening the output report

If we have a lot of tests and make a chance that results in multiple
failure we can change the length of the traceback report that gets 
shown.  We can make it short:

```bash
$ pytest --tb=short
```

### Show local variables

We can also tell pytest to show us the values of different locally
defined variables in the test.

Let's update `test_double` to include two extra lines for defining some
variables.

```python
def test_doubling_two():
    """Test running double on two."""
    x = 1
    y = 2
    assert double(2) == 4
```

Then we can use `--show-locals` to show us the values of each of the 
variables that got defined.

```bash
$ pytest --show-locals
```

We'll delete those two extra lines before moving on.## Markers

[decorators]: https://docs.python.org/3/glossary.html#term-decorator

There are a bunch of [decorators] in `pytest` that we can use to mark
tests.  These markers can tell `pytest` to do a variety of things 

A decorator is in its essence, a function that operates on a function,
where we wrap one function around another in order to modify its
behavior.  Decorators are denoted with the `@` symbol.

### Skipping tests

We can use `@pytest.mark.skip` to tell `pytest` to skip a test function.

```python
import pytest

@pytest.mark.skip
def test_double():
    assert double(2) == 4
```

Then we can run pytest.

```bash
$ pytest
```

Only one test was run.

### Marking tests as expected to fail

Occasionally, we will end up having tests that we know are failing. The
failing tests might be for functionality that still needs to be written,
or perhaps for a bug that we know about but are not yet able to fix. 
To mark a test as expected to fail, we can use the `pytest.mark.fail`
decorator.

```python
@pytest.mark.xfail(reason="The function isn't working.")
def test_double():
    assert double(2) == 4
```

Then we can run pytest.

```bash
$ pytest
```

Both tests were run, but the failing test is marked with an `X` since
it was expected to fail.
## Test parametrization

From the previous section, `test_double.py` is currently this:

```python
def double(n):
    """Double the argument."""
    return 2 * n

def test_doubling_one():
    assert double(1) == 2

def test_doubling_two():
    assert double(2) == 4
```

The last two tests are doing the same thing, except for different numbers.
What if we could write one test that did this for both?

```python
def test_double(argument, expected):
    assert double(argument) == expected
```

We can use `@pytest.mark.parametrize` decorator.  If you've not used 
a decorator before, it's essentially a function that operates on a
function.  With `@pytest.mark.parametrize`, 

```python
import pytest

@pytest.mark.parametrize(
    "argument, expected",
    [
        (1, 2),
        (2, 4),
        (4, 8),
        (0, 0),
        (-1, -2),
        (500, 1000)
    ],
)
def test_double(argument, expected):
    assert double(argument) == expected
```

Now let's run pytest.

```bash
$ pytest
```

The six dots mean that everything passed.## Testing exceptions

Now let's suppose that for our application, we want `double` to work 
with numbers and not strings.  If given a string, `double` should raise
a `TypeError`.  It is important that we write tests not only for the 
happy path where everything is working as intended, but also for cases
where problems occur.  We need to make sure our code *fails* correctly.

Chances are we would write the code first and then the test, but let's 
see what happens when we write the test first.  This is called
**test-driven development**.

But first, how do we test an exception?  We can do that with the
`pytest.raises` context manager.

```python
def test_double_exception():
    with pytest.raises(TypeError):
        double("invalid input")  # be descriptive here
```

Now let's run the tests again.  This time, we are expecting it to fail,
and it does!

```bash
$ pytest
```

Now let's go in and see what happens when we raise the wrong error.

```python
def double(n):
    """Double the argument."""

    if isinstance(n, str):
        raise ValueError
    
    return 2 * n
```


```bash
$ pytest
```

The test failed because we raised the wrong exception.  But the failure report is
quite a lot, so let's run this with ``--tb=short``.  This option shortens what
gets reported.  I use this option a lot, especially when I change something and
then get 259 test failures.  

```bash
$ pytest --tb=short
```

Now let's go in and actually fix this.  

```bash
$ pytest
```

It passes, and all is well in the universe once again. Similarly, we can
also use `pytest.warns` to check for warnings in much the same way as we
use `pytest.raises` to check for exceptions.## Testing functions in a Python file

Let's create a file called `module.py` and put a function in it called
`triple`.

```python
def triple(x):
    """Triple the argument."""
    return 3 * x
```

Now let's create a file called `test_module.py` to test `triple`.

```python
from module import triple

def test_triple():
    assert triple(3) == 9
```

And now let's run pytest.

```bash
$ pytest
```

And we see that pytest finds and runs the test, and it passes.
