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

The six dots mean that everything passed.