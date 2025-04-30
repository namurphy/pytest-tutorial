## Testing functions in a Python file

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
