import pytest
from src.assignment1 import add_matrices  # Import the function

def test_add_matrices():
    A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    B = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
    expected_result = [[10, 10, 10], [10, 10, 10], [10, 10, 10]]

    assert add_matrices(A, B) == expected_result
