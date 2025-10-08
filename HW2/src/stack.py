class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        '''пустой стек'''
        self.top = None
        self._size = 0

    def push(self, item):
        '''добавление элемента в вершину стека'''
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node
        self._size += 1

    def pop(self):
        '''удаление и возврат верхнего элемента стека'''
        if self.is_empty():
            raise IndexError("попытка извлечь элемент из пустого стека")
        item = self.top.data
        self.top = self.top.next
        self._size -= 1
        return item

    def peek(self):
        '''просмотр верхнего элемента без удаления'''
        if self.is_empty():
            raise IndexError("попытка просмотра пустого стека")
        return self.top.data

    def is_empty(self):
        '''проверка на заполненность'''
        return self._size == 0

    def size(self):
        '''размер стека'''
        return self._size