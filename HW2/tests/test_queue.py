import pytest
from src.queue import Queue

def test_enqueue_dequeue():
    '''добавление и извлечение элементов'''
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    assert queue.dequeue() == 1
    assert queue.dequeue() == 2
    assert queue.dequeue() == 3

def test_peek():
    '''просмотр первого элемента'''
    queue = Queue()
    queue.enqueue(42)
    assert queue.peek() == 42
    assert queue.size() == 1  # не удаляется при peek

def test_is_empty():
    '''проверка пустоты очереди'''
    queue = Queue()
    assert queue.is_empty() == True
    queue.enqueue(1)
    assert queue.is_empty() == False

def test_size():
    '''размер очереди'''
    queue = Queue()
    assert queue.size() == 0
    queue.enqueue(1)
    queue.enqueue(2)
    assert queue.size() == 2

def test_dequeue_empty():
    '''ошибка при извлечении из пустой очереди'''
    queue = Queue()
    with pytest.raises(IndexError, match="попытка извлечь элемент из пустой очереди"):
        queue.dequeue()

def test_peek_empty():
    '''ошибка при просмотре пустой очереди'''
    queue = Queue()
    with pytest.raises(IndexError, match="попытка просмотра пустой очереди"):
        queue.peek()