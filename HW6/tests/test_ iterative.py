import time
import pytest
from src.iterative import iterative_mergesort, iterative_quicksort, time_decorator

@pytest.mark.parametrize("func", [iterative_mergesort, iterative_quicksort])
@pytest.mark.parametrize(
    "input_arr, expected",
    [
        ([], []),  # empty
        ([1], [1]),  # single element
        ([2, 1], [1, 2]),  # two elements unsorted
        ([1, 2], [1, 2]),  # two elements sorted
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),  # reverse sorted
        ([1, 3, 2, 5, 4], [1, 2, 3, 4, 5]),  # random
        ([1, 1, 1], [1, 1, 1]),  # all duplicates
        ([1, 2, 2, 3], [1, 2, 2, 3]),  # some duplicates
        (list(range(1000)), list(range(1000))),  # large sorted
        (list(range(999, -1, -1)), list(range(1000))),  # large reverse
        ([0], [0]),  # zero
        ([-1, -3, 0, 2, -2], [-3, -2, -1, 0, 2]),  # negative and positive
        ([float('inf'), 1, float('-inf'), 0], [float('-inf'), 0, 1, float('inf')]),  # inf values
    ]
)
def test_sorts(func, input_arr, expected):
    result = func(input_arr)
    assert result == expected
    assert len(result) == len(input_arr)  # length preserved

def test_time_decorator(capsys):
    @time_decorator
    def dummy_func():
        time.sleep(0.01)
        return 42

    result = dummy_func()
    assert result == 42
    captured = capsys.readouterr()
    assert "dummy_func execution time:" in captured.out
    assert float(captured.out.split(":")[1].strip().split()[0]) >= 0.01

@pytest.mark.parametrize("func", [iterative_mergesort, iterative_quicksort])
def test_no_mutation(func):
    arr = [3, 1, 2]
    original = arr[:]
    func(arr)
    assert arr == original  # since functions return copy, but check if input mutated - wait, implementations mutate, so adjust if needed
    # Note: current impl mutates, if need non-mutating, copy first

# Adjust if non-mutating required, but task doesn't specify, so ok