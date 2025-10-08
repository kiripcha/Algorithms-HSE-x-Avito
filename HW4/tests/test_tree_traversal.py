import pytest
from src.tree_traversal import BST

def test_empty_tree():
    '''пусток дерево'''
    bst = BST()
    assert bst.pre_order() == []
    assert bst.post_order() == []
    assert bst.in_order() == []
    assert bst.reverse_pre_order() == []
    assert bst.reverse_post_order() == []
    assert bst.reverse_in_order() == []

def test_single_node():
    '''дерево с одним узлом'''
    bst = BST()
    bst.insert(5)
    assert bst.pre_order() == [5]
    assert bst.post_order() == [5]
    assert bst.in_order() == [5]
    assert bst.reverse_pre_order() == [5]
    assert bst.reverse_post_order() == [5]
    assert bst.reverse_in_order() == [5]

def test_balanced_tree():
    '''сбалансированное дерево'''
    bst = BST()
    values = [5, 3, 7, 1, 4, 6, 8]
    for value in values:
        bst.insert(value)
    # Дерево:
    #       5
    #      / \
    #     3   7
    #    / \  / \
    #   1   4 6  8
    assert bst.pre_order() == [5, 3, 1, 4, 7, 6, 8]
    assert bst.post_order() == [1, 4, 3, 6, 8, 7, 5]
    assert bst.in_order() == [1, 3, 4, 5, 6, 7, 8]
    assert bst.reverse_pre_order() == [5, 7, 8, 6, 3, 4, 1]
    assert bst.reverse_post_order() == [8, 6, 7, 4, 1, 3, 5]
    assert bst.reverse_in_order() == [8, 7, 6, 5, 4, 3, 1]

def test_unbalanced_tree():
    '''несбалансированное дерево'''
    bst = BST()
    values = [1, 2, 3, 4]
    for value in values:
        bst.insert(value)
    # Дерево:
    #   1
    #    \
    #     2
    #      \
    #       3
    #        \
    #         4
    assert bst.pre_order() == [1, 2, 3, 4]
    assert bst.post_order() == [4, 3, 2, 1]
    assert bst.in_order() == [1, 2, 3, 4]
    assert bst.reverse_pre_order() == [1, 4, 3, 2]
    assert bst.reverse_post_order() == [4, 3, 2, 1]
    assert bst.reverse_in_order() == [4, 3, 2, 1]