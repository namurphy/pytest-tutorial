## Assertions

An `assert` statement allows us to check whether a particular condition
is true. If we assert something true, then nothing happens.

```pycon
>>> assert True
```

If we assert something false, then we get an `AssertionError`.

```pycon
>>> assert False
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AssertionError
```

We can use `assert` statements in a few ways. We could put them directly
into code that we write 

We can use this to test software.

```pycon
>>> assert 1 == 1
```

Now let's create a failing test.

```pycon
>>> assert 6 * 9 == 42
```

We can also add an error message!

```pycon
>>> assert [1, 2] == [3, 4], "List contents are not equal."
```

## Exceptions

An exception is an error that happens when Python code is being executed.
An example is a `ZeroDivisionError`.

```pycon
>>> 1 / 0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
```

We can also raise our own exceptions.

```pycon
>>> raise ValueError
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError
```

We can even add our own error messages.

```pycon
>>> raise ValueError("We can add error messages here too!")
```

We can also handle exceptions 

```pycon
>>> x = 1
>>> y = 0
>>> try:
...     x / y
... except ZeroDivisionError:
...     print("Attempting to divide by zero.")
... else:
...     print("Not attempting to divide by zero")
Attempting to divide by zero.
```

