import pytest
from src.validate_stack import validate_stack_sequences

def test_valid_sequence():
    '''валидная последовательность'''
    pushed = [1, 2, 3, 4, 5]
    popped = [1, 3, 5, 4, 2]
    assert validate_stack_sequences(pushed, popped) == True

def test_invalid_sequence():
    '''невалидная последовательность'''
    pushed = [1, 2, 3]
    popped = [3, 1, 2]
    assert validate_stack_sequences(pushed, popped) == False

def test_empty_sequences():
    '''пустые последовательности'''
    assert validate_stack_sequences([], []) == True

def test_single_element():
    '''с одним элементом'''
    assert validate_stack_sequences([1], [1]) == True
    assert validate_stack_sequences([1], [2]) == False

def test_long_valid_sequence():
    '''длинная валидная последовательность'''
    pushed = [1, 2, 3, 4, 5, 6, 7, 8]
    popped = [1, 2, 3, 4, 8, 7, 6, 5]
    assert validate_stack_sequences(pushed, popped) == True

def test_long_invalid_sequence():
    '''длинная невалидная последовательность'''
    pushed = [1, 2, 3, 4, 5, 6, 7, 8]
    popped = [8, 7, 6, 5, 4, 3, 2, 1]
    assert validate_stack_sequences(pushed, popped) == False

def test_interleaved_sequence():
    '''последовательность с чередованием push/pop'''
    pushed = [1, 2, 3, 4]
    popped = [2, 1, 4, 3]
    assert validate_stack_sequences(pushed, popped) == True