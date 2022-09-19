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

We'll delete those two extra lines before moving on.