## Creating and running a test

First of all, let's install pytest.

```bash
$ python -m pip install pytest
```

Let's make sure it installed okay.

```bash
$ pytest --version
pytest 7.1.3
```

Now let's create and enter a directory to work in.

```bash
mkdir first_tests
cd first_tests
```

Now let's create a file called `test_double.py`.  It's important that the
name begin with `test_` since that is how pytest will know that it
includes tests to be run.  In it, let's create a function called 
`double`, and introduce an intentional bug.  Let's also write a test
called `test_doubling_one`.

```python
def double(n):
    """Double the argument."""
    return n + 1  # intentional bug

def test_doubling_one():
    assert double(1) == 2
```

Let's go back to our terminal and run `pytest`.

```bash
$ pytest
```

This means that the tests ran, and we  

```python
def test_doubling_two():
    assert double(2) == 4
```

And let's run pytest again too.

```bash
$ pytest
```

This time we got a failure