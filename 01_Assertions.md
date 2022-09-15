## Assertions

An `assert` statement allows us to check whether a particular condition
is true.

If we assert something true, then nothing happens.

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
