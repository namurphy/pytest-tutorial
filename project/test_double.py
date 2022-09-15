import pytest

def double(n):
    """Double the argument."""

    if isinstance(n, str):
        raise TypeError
    
    return 2 * n

@pytest.mark.parametrize(
    "argument, expected",
    [
        (1, 2),
        (2, 4),
        (4, 8),
        (0, 0),
        (-1, -2),
        (500, 1000)
    ],
)
def test_double(argument, expected):
    assert double(argument) == expected


def test_double_exception():
    with pytest.raises(TypeError):
        double("invalid input")  # be descriptive here
