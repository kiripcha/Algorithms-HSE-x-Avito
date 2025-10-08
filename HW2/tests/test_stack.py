import pytest
from src.stack import Stack

def test_push_pop():
    '''добавление и извлечение элементов'''
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.pop() == 3
    assert stack.pop() == 2
    assert stack.pop() == 1

def test_peek():
    '''просмотр верхнего элемента'''
    stack = Stack()
    stack.push(42)
    assert stack.peek() == 42
    assert stack.size() == 1  # не удаляется при peek

def test_is_empty():
    '''проверка пустоты стека'''
    stack = Stack()
    assert stack.is_empty() == True
    stack.push(1)
    assert stack.is_empty() == False

def test_size():
    '''размер стека'''
    stack = Stack()
    assert stack.size() == 0
    stack.push(1)
    stack.push(2)
    assert stack.size() == 2

def test_pop_empty():
    '''ошибка при извлечении из пустого стека'''
    stack = Stack()
    with pytest.raises(IndexError, match="попытка извлечь элемент из пустого стека"):
        stack.pop()

def test_peek_empty():
    '''ошибка при просмотре пустого стека'''
    stack = Stack()
    with pytest.raises(IndexError, match="попытка просмотра пустого стека"):
        stack.peek()