## Markers

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
