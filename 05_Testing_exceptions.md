## Testing exceptions

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
======================================= test session starts ========================================
platform linux -- Python 3.10.4, pytest-7.1.3, pluggy-1.0.0
rootdir: /home/namurphy/Projects/pytest-tutorial/project
plugins: datadir-1.3.1, forked-1.4.0, hypothesis-6.54.5, regressions-2.3.1, xdist-2.5.0, anyio-3.6.1
collected 7 items                                                                                  

test_double.py ......F                                                                       [100%]

============================================= FAILURES =============================================
______________________________________ test_double_exception _______________________________________

    def test_double_exception():
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

test_double.py:23: Failed
===================================== short test summary info ======================================
FAILED test_double.py::test_double_exception - Failed: DID NOT RAISE <class 'TypeError'>
=================================== 1 failed, 6 passed in 0.09s ====================================
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
======================================= test session starts ========================================
platform linux -- Python 3.10.4, pytest-7.1.3, pluggy-1.0.0
rootdir: /home/namurphy/Projects/pytest-tutorial/project
plugins: datadir-1.3.1, forked-1.4.0, hypothesis-6.54.5, regressions-2.3.1, xdist-2.5.0, anyio-3.6.1
collected 7 items                                                                                  

test_double.py ......F                                                                       [100%]

============================================= FAILURES =============================================
______________________________________ test_double_exception _______________________________________

    def test_double_exception():
        with pytest.raises(TypeError):
>           double("invalid input")  # be descriptive here

test_double.py:28: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

n = 'invalid input'

    def double(n):
        """Double the argument."""
    
        if isinstance(n, str):
>           raise ValueError
E           ValueError

test_double.py:7: ValueError
===================================== short test summary info ======================================
FAILED test_double.py::test_double_exception - ValueError
=================================== 1 failed, 6 passed in 0.09s ====================================
```

The test failed because we raised the wrong exception.  But the failure report is
quite a lot, so let's run this with ``--tb=short``.  This option shortens what
gets reported.  I use this option a lot, especially when I change something and
then get 259 test failures.  

```bash
$ pytest --tb=short
======================================= test session starts ========================================
platform linux -- Python 3.10.4, pytest-7.1.3, pluggy-1.0.0
rootdir: /home/namurphy/Projects/pytest-tutorial/project
plugins: datadir-1.3.1, forked-1.4.0, hypothesis-6.54.5, regressions-2.3.1, xdist-2.5.0, anyio-3.6.1
collected 7 items                                                                                  

test_double.py ......F                                                                       [100%]

============================================= FAILURES =============================================
______________________________________ test_double_exception _______________________________________
test_double.py:28: in test_double_exception
    double("invalid input")  # be descriptive here
test_double.py:7: in double
    raise ValueError
E   ValueError
===================================== short test summary info ======================================
FAILED test_double.py::test_double_exception - ValueError
=================================== 1 failed, 6 passed in 0.09s ====================================
```

Now let's go in and actually fix this.  

```bash
$ pytest
======================================= test session starts ========================================
platform linux -- Python 3.10.4, pytest-7.1.3, pluggy-1.0.0
rootdir: /home/namurphy/Projects/pytest-tutorial/project
plugins: datadir-1.3.1, forked-1.4.0, hypothesis-6.54.5, regressions-2.3.1, xdist-2.5.0, anyio-3.6.1
collected 7 items                                                                                  

test_double.py .......                                                                       [100%]

======================================== 7 passed in 0.02s =========================================
```

It passes, and all is well in the universe once again. Similarly, we can
also use `pytest.warns` to check for warnings in much the same way as we
use `pytest.raises` to check for exceptions.