import pytest
from src.validate_bst import Node, is_valid_bst

def create_bst(values):
    if not values:
        return None
    root = Node(values[0])
    for value in values[1:]:
        current = root
        while True:
            if value < current.value:
                if current.left is None:
                    current.left = Node(value)
                    break
                current = current.left
            else:
                if current.right is None:
                    current.right = Node(value)
                    break
                current = current.right
    return root

def test_empty_tree():
    '''пустое дерево'''
    assert is_valid_bst(None) == True

def test_single_node():
    '''деревья с одним узлом'''
    root = Node(5)
    assert is_valid_bst(root) == True

def test_valid_bst():
    '''корректного BST'''
    # Дерево:
    #       5
    #      / \
    #     3   7
    #    / \  / \
    #   1   4 6  8
    root = create_bst([5, 3, 7, 1, 4, 6, 8])
    assert is_valid_bst(root) == True

def test_invalid_bst():
    '''некорректное BST'''
    # Дерево:
    #       5
    #      / \
    #     3   7
    #    / \
    #   4   2 (4 > 3, что нарушает правило BST)
    root = Node(5)
    root.left = Node(3)
    root.right = Node(7)
    root.left.left = Node(4)
    root.left.right = Node(2)
    assert is_valid_bst(root) == False

def test_unbalanced_bst():
    '''несбалансированное BST'''
    # Дерево:
    #   1
    #    \
    #     2
    #      \
    #       3
    root = create_bst([1, 2, 3])
    assert is_valid_bst(root) == True

def test_invalid_unbalanced():
    '''некорректное несбалансированное дерево'''
    # Дерево:
    #   1
    #    \
    #     3
    #    /
    #   2 (2 < 3, но находится в левом поддереве)
    root = Node(1)
    root.right = Node(3)
    root.right.left = Node(2)
    assert is_valid_bst(root) == False

def test_duplicate_values():
    '''с дубликатами'''
    # Дерево:
    #       5
    #      / \
    #     3   5
    root = Node(5)
    root.left = Node(3)
    root.right = Node(5)
    assert is_valid_bst(root) == True

def test_invalid_duplicate_values():
    '''некорректное дерево с дубликатами'''
    # Дерево:
    #       5
    #      /
    #     5 (дубликат в левом поддереве)
    root = Node(5)
    root.left = Node(5)
    assert is_valid_bst(root) == False

def test_large_values():
    '''с граничными значениями'''
    # Дерево:
    #       0
    #      / \
    #   -inf  inf
    root = Node(0)
    root.left = Node(float('-inf'))
    root.right = Node(float('inf'))
    assert is_valid_bst(root) == True

def test_invalid_large_values():
    '''некорректное дерево с граничными значениями'''
    # Дерево:
    #       0
    #      /
    #    inf (inf в левом поддереве)
    root = Node(0)
    root.left = Node(float('inf'))
    assert is_valid_bst(root) == False