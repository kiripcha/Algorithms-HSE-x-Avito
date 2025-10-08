class Node:
    '''проверка бинарного дерева поиска (BST)'''
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def is_valid_bst(root):
    '''является ли бинарное дерево бинарным деревом поиска'''
    def validate(node, min_value, max_value):
        if not node:
            return True
        # значение узла находится в допустимом диапазоне
        if node.value <= min_value or node.value >= max_value:
            return False
        # рекурсивно проверяем левое и правое поддеревья
        return validate(node.left, min_value, node.value) and validate(node.right, node.value, max_value)
    
    return validate(root, float('-inf'), float('inf'))