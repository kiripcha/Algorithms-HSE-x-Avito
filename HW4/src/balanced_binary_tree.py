class Node:
    '''проверка сбалансированности бинарного дерева'''
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def is_balanced(root):
    '''Проверяет, является ли бинарное дерево сбалансированным по высоте.
    Возвращает True, если для каждого узла разница высот поддеревьев <= 1, иначе False.'''
    def check_height(node):
        if not node:
            return 0
        left_height = check_height(node.left)
        right_height = check_height(node.right)
        if left_height == -1 or right_height == -1:
            return -1
        if abs(left_height - right_height) > 1:
            return -1
        return max(left_height, right_height) + 1
    
    return check_height(root) != -1