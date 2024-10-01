import pathlib
import random
import sys


import pytest


sys.path.insert(
    0,
    pathlib.Path(__file__).parent.parent.resolve(),
)

import exercise


# --- Tests ---

def test_exercise_add():
    """Tests the add function with various inputs."""
    # Test with positive numbers
    assert exercise.add(5, 3) == 8
    assert exercise.add(10, 20) == 30
    # Test with negative numbers
    assert exercise.add(-5, 3) == -2
    assert exercise.add(10, -20) == -10
    # Test with zero
    assert exercise.add(0, 0) == 0
    assert exercise.add(5, 0) == 5


def test_exercise_sub():
    """Tests the sub function with various inputs."""
    assert exercise.sub(5, 3) == 2
    assert exercise.sub(20, 10) == 10
    assert exercise.sub(-5, 3) == -8
    assert exercise.sub(10, -20) == 30
    assert exercise.sub(0, 0) == 0
    assert exercise.sub(5, 0) == 5


def test_exercise_mul():
    """Tests the mul function with various inputs."""
    assert exercise.mul(5, 3) == 15
    assert exercise.mul(10, 20) == 200
    assert exercise.mul(-5, 3) == -15
    assert exercise.mul(10, -20) == -200
    assert exercise.mul(0, 0) == 0
    assert exercise.mul(5, 0) == 0


def test_exercise_div():
    """Tests the div function with various inputs, including division by zero."""
    assert exercise.div(10, 2) == 5
    assert exercise.div(20, 5) == 4
    assert exercise.div(-10, 2) == -5
    assert exercise.div(10, -2) == -5
    assert exercise.div(0, 5) == 0
    # Test division by zero

    msg = "0으로 나누려고 하면 'Cannot divide by zero'라는 문자열을 대신 반환 바랍니다."

    result_div_by_zero = None

    with pytest.raises(ZeroDivisionError):
        result_div_by_zero = exercise.div(5, 0), msg
    assert 'Cannot divide by zero' == result_div_by_zero, msg


def test_random_inputs():
    """Tests all functions with random inputs."""
    for _ in range(10):  # Run 10 random tests
        a = random.randint(-100, 100)
        b = random.randint(-100, 100)

        # Skip division by zero in random tests
        if b == 0:
            b = random.randint(2, 100) * random.choice((-1, 1))

        assert exercise.add(a, b) == a + b
        assert exercise.sub(a, b) == a - b
        assert exercise.mul(a, b) == a * b
        assert exercise.div(a, b) == a / b


if __name__ == "__main__":
    pytest.main([__file__])
