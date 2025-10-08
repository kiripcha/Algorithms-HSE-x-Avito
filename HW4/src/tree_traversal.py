# Реализация бинарного дерева поиска (BST) и всех обходов

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        '''инициализирует пустое бинарное дерево поиска'''
        self.root = None

    def insert(self, value):
        '''вставляет значение в бинарное дерево поиска'''
        if not self.root:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        # Вспомогательная функция для рекурсивной вставки
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)

    def pre_order(self):
        '''pre-order обход: корень → левое поддерево → правое поддерево'''
        result = []
        self._pre_order_recursive(self.root, result)
        return result

    def _pre_order_recursive(self, node, result):
        if node:
            result.append(node.value)
            self._pre_order_recursive(node.left, result)
            self._pre_order_recursive(node.right, result)

    def post_order(self):
        '''post-order обход: левое поддерево → правое поддерево → корень'''
        result = []
        self._post_order_recursive(self.root, result)
        return result

    def _post_order_recursive(self, node, result):
        if node:
            self._post_order_recursive(node.left, result)
            self._post_order_recursive(node.right, result)
            result.append(node.value)

    def in_order(self):
        '''in-order обход: левое поддерево → корень → правое поддерево'''
        result = []
        self._in_order_recursive(self.root, result)
        return result

    def _in_order_recursive(self, node, result):
        if node:
            self._in_order_recursive(node.left, result)
            result.append(node.value)
            self._in_order_recursive(node.right, result)

    def reverse_pre_order(self):
        '''reverse pre-order обход: корень → правое поддерево → левое поддерево'''
        result = []
        self._reverse_pre_order_recursive(self.root, result)
        return result

    def _reverse_pre_order_recursive(self, node, result):
        if node:
            result.append(node.value)
            self._reverse_pre_order_recursive(node.right, result)
            self._reverse_pre_order_recursive(node.left, result)

    def reverse_post_order(self):
        '''reverse post-order обход: правое поддерево → левое поддерево → корень'''
        result = []
        self._reverse_post_order_recursive(self.root, result)
        return result

    def _reverse_post_order_recursive(self, node, result):
        if node:
            self._reverse_post_order_recursive(node.right, result)
            self._reverse_post_order_recursive(node.left, result)
            result.append(node.value)

    def reverse_in_order(self):
        '''reverse in-order обход: правое поддерево → корень → левое поддерево'''
        result = []
        self._reverse_in_order_recursive(self.root, result)
        return result

    def _reverse_in_order_recursive(self, node, result):
        if node:
            self._reverse_in_order_recursive(node.right, result)
            result.append(node.value)
            self._reverse_in_order_recursive(node.left, result)