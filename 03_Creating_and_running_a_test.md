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
======================================= test session starts ========================================
platform linux -- Python 3.10.4, pytest-7.1.3, pluggy-1.0.0
rootdir: /home/namurphy/Projects/pytest-tutorial/project
plugins: datadir-1.3.1, forked-1.4.0, hypothesis-6.54.5, regressions-2.3.1, xdist-2.5.0, anyio-3.6.1
collected 1 item                                                                                   

test_double.py .                                                                             [100%]

======================================== 1 passed in 0.01s =========================================
```

This means that the tests ran, and we  

```python
def test_doubling_two():
    assert double(2) == 4
```

And let's run pytest again too.

```bash
$ pytest
======================================= test session starts ========================================
platform linux -- Python 3.10.4, pytest-7.1.3, pluggy-1.0.0
rootdir: /home/namurphy/Projects/pytest-tutorial/project
plugins: datadir-1.3.1, forked-1.4.0, hypothesis-6.54.5, regressions-2.3.1, xdist-2.5.0, anyio-3.6.1
collected 2 items                                                                                  

test_double.py .F                                                                            [100%]

============================================= FAILURES =============================================
________________________________________ test_doubling_two _________________________________________

    def test_doubling_two():
>       assert double(2) == 4
E       assert 3 == 4
E        +  where 3 = double(2)

test_double.py:10: AssertionError
===================================== short test summary info ======================================
FAILED test_double.py::test_doubling_two - assert 3 == 4
=================================== 1 failed, 1 passed in 0.09s ====================================
```

This time we got a test failure — which is good because we were able to find a
bug soon after we introduced it.  Now we can fix it!

```python
def double(n):
    """Double the argument."""
    return 2 * n  # nox fixed
```

Let's now run `pytest` again, but let's used the `--last-failed` option,
which will run only the tests that failed last time (or all tests, if
none failed).

```bash
$ pytest --last-failed
======================================= test session starts ========================================
platform linux -- Python 3.10.4, pytest-7.1.3, pluggy-1.0.0
rootdir: /home/namurphy/Projects/pytest-tutorial/project
plugins: datadir-1.3.1, forked-1.4.0, hypothesis-6.54.5, regressions-2.3.1, xdist-2.5.0, anyio-3.6.1
collected 1 item                                                                                   
run-last-failure: rerun previous 1 failure

test_double.py .                                                                             [100%]

======================================== 1 passed in 0.01s =========================================
```

Now all is good in the universe.