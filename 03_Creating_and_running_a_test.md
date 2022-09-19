## Creating and running a test

First of all, let's install and upgrade pytest. To use `pip` we can do:

```bash
$ pip install -U pytest
```

Let's make sure it installed okay. 

```bash
$ pytest --version
pytest 7.1.3
```

Now let's create and enter a directory to work in.

```bash
mkdir pytest_tutorial
cd pytest_tutorial
```

Now let's create a file called `test_double.py`.  It's important that the
name begin with `test_` since that is how `pytest` will know that it
includes tests to be run.  

In `test_double.py`, let's create a function called `double`, and 
introduce an intentional error.  Let's also write a test called 
`test_doubling_one` that is designed to pass even with the error that
we purposefully introduced. 

```python
def double(n):
    """Double the argument."""
    return n + 1  # intentional error

def test_doubling_one():
    """Test running double on one."""
    assert double(1) == 2  # will pass even with intentional error
```

Again, the name is important. Its name starts with `test_` so that 
`pytest` will know that it's a test that it  should run. 

Let's go back to our terminal and run `pytest`.

```bash
$ pytest
============================== test session starts ===============================
platform linux -- Python 3.9.12, pytest-7.1.3, pluggy-1.0.0
rootdir: /home/namurphy/pytest_tutorial
plugins: datadir-1.3.1, forked-1.4.0, xonsh-0.12.6, anyio-3.6.1, xdist-2.5.0
collected 1 item                                                                 

test_double.py .                                                           [100%]

=============================== 1 passed in 0.02s ================================
```

The output shows the platform, the versions of Python and other packages
that we used, the directory the tests are running in, and possibly a set
of plugins. The output shows that it collected one item (i.e., one test)
from `test_double.py`. The `.` next to `test_double.py` means that the
test passed.

Now let's add another test that we know will catch the error that we put
into `double`.

```python
def test_doubling_two():
    """Test running double on two."""
    assert double(2) == 4
```

And let's run pytest again.

```bash
$ pytest
============================== test session starts ===============================
platform linux -- Python 3.9.12, pytest-7.1.3, pluggy-1.0.0
rootdir: /home/namurphy/pytest_tutorial
plugins: datadir-1.3.1, forked-1.4.0, xonsh-0.12.6, anyio-3.6.1, xdist-2.5.0
collected 2 items                                                                

test_double.py .F                                                          [100%]

==================================== FAILURES ====================================
_______________________________ test_doubling_two ________________________________

    def test_doubling_two():
        """Test running double on two."""
>       assert double(2) == 4
E       assert 3 == 4
E        +  where 3 = double(2)

test_double.py:10: AssertionError
============================ short test summary info =============================
FAILED test_double.py::test_doubling_two - assert 3 == 4
========================== 1 failed, 1 passed in 0.11s ===========================

```

This time we got a failure, as expected!

Now it says it collected two items.  The `.` means that the first test
passed, and the `F` means that the second test failed. It then gives a
failure report. It shows the `assert` statement, and puts in the values
for the left and right sides of the equality comparison. This diagnostic
information helps us figure out what happened.

We're going to keep one test passing and one test failing as we move
onto the next section.
