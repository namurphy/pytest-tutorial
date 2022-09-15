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
======================================= test session starts ========================================
platform linux -- Python 3.10.4, pytest-7.1.3, pluggy-1.0.0
rootdir: /home/namurphy/Projects/pytest-tutorial/project
plugins: datadir-1.3.1, forked-1.4.0, hypothesis-6.54.5, regressions-2.3.1, xdist-2.5.0, anyio-3.6.1
collected 6 items                                                                                  

test_double.py ......                                                                        [100%]

======================================== 6 passed in 0.02s =========================================
```

The six dots mean that everything passed.