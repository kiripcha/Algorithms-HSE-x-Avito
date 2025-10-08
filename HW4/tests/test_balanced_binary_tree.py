import pytest
from src.balanced_binary_tree import Node, is_balanced

def test_empty_tree():
    '''пустое дерево'''
    assert is_balanced(None) == True

def test_single_node():
    '''деревья с одним узлом (сбалансированные)'''
    root = Node(1)
    assert is_balanced(root) == True

def test_balanced_two_nodes():
    '''сбалансированное дерево с двумя узлами'''
    root = Node(1)
    root.left = Node(2)
    assert is_balanced(root) == True

def test_balanced_three_nodes():
    '''сбалансированное дерево с тремя узлами'''
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    assert is_balanced(root) == True

def test_unbalanced_left_heavy():
    '''несбалансированного дерева (левое поддерево глубже на 2)'''
    # Дерево:
    #   1
    #  /
    # 2
    # /
    # 3
    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(3)
    assert is_balanced(root) == False

def test_unbalanced_right_heavy():
    '''несбалансированное дерево (правое поддерево глубже на 2)'''
    # Дерево:
    #   1
    #    \
    #     2
    #      \
    #       3
    root = Node(1)
    root.right = Node(2)
    root.right.right = Node(3)
    assert is_balanced(root) == False

def test_balanced_with_diff_one():
    '''сбалансированное дерево с разницей высот = 1'''
    # Дерево:
    #       1
    #      / \
    #     2   3
    #    /     \
    #   4       5
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.right = Node(5)
    assert is_balanced(root) == True

def test_unbalanced_in_subtree():
    '''деревья, где несбалансированность в поддереве'''
    # Дерево:
    #       1
    #      /
    #     2
    #    /
    #   3
    #  /
    # 4
    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(3)
    root.left.left.left = Node(4)
    assert is_balanced(root) == False

def test_fully_balanced():
    '''полностью сбалансированное дерево (бинарное)'''
    # Дерево:
    #       1
    #      / \
    #     2   3
    #    / \ /
    #   4  5 6
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    assert is_balanced(root) == True

def test_one_side_tree_balanced():
    '''деревья с одним поддеревом'''
    # Для высоты 2: сбалансировано
    # Дерево:
    #   1
    #    \
    #     2
    root = Node(1)
    root.right = Node(2)
    assert is_balanced(root) == True

def test_tree_with_none_subtrees():
    '''деревья с None в поддеревьях'''
    root = Node(1)
    root.left = None
    root.right = Node(2)
    root.right.left = None
    root.right.right = None
    assert is_balanced(root) == True