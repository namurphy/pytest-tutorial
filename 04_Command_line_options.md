## Command line options

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

### Running only the tests that failed last time

If we have a bunch of tests or tests that take a long time to run, we 
can use the ``--last-failed`` option which will run only the tests that
failed the last time that we ran the tests.  (If no tests failed, it
will run all the tests.)

```bash
$ pytest
$ pytest --last-failed
```

### Shortening the output report

If we have a lot of tests and make a chance that results in multiple
failure we can change the length of the traceback report that gets 
shown.  We can make it short:

```bash
$ pytest --tb=short
```

### Getting help

To see what command line options are available for pytest, we can run

```bash
pytest --help
```

There are a lot!