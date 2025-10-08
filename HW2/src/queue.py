class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        '''инициализация пустой очереди'''
        self.front = None
        self.rear = None
        self._size = 0

    def enqueue(self, item):
        '''добавление элемента в конец очереди'''
        new_node = Node(item)
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self._size += 1

    def dequeue(self):
        '''удаление и возврат элемента из начала очереди'''
        if self.is_empty():
            raise IndexError("попытка извлечь элемент из пустой очереди")
        item = self.front.data
        self.front = self.front.next
        self._size -= 1
        if self.is_empty():
            self.rear = None
        return item

    def peek(self):
        '''просмотр первого элемента без удаления'''
        if self.is_empty():
            raise IndexError("попытка просмотра пустой очереди")
        return self.front.data

    def is_empty(self):
        '''проверка на заполненность'''
        return self._size == 0

    def size(self):
        '''рамзер очереди'''
        return self._size