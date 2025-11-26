from __future__ import annotations
from typing import Optional, Any
from src.tracer import trace


class AVLNode:
    def __init__(self, key: Any):
        self.key = key
        self.height = 1
        self.left: Optional[AVLNode] = None
        self.right: Optional[AVLNode] = None


class AVL:
    def __init__(self):
        self.root: Optional[AVLNode] = None

    def _height(self, node: Optional[AVLNode]) -> int:
        return node.height if node else 0

    def _update_height(self, node: AVLNode):
        node.height = 1 + max(self._height(node.left), self._height(node.right))

    def _balance_factor(self, node: Optional[AVLNode]) -> int:
        return self._height(node.right) - self._height(node.left) if node else 0

    def _rotate_left(self, z: AVLNode) -> AVLNode:
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        self._update_height(z)
        self._update_height(y)
        return y

    def _rotate_right(self, z: AVLNode) -> AVLNode:
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        self._update_height(z)
        self._update_height(y)
        return y

    def _balance(self, node: AVLNode) -> AVLNode:
        self._update_height(node)

        balance = self._balance_factor(node)

        if balance < -1:
            if self._balance_factor(node.left) > 0:
                node.left = self._rotate_left(node.left)
            return self._rotate_right(node)

        if balance > 1:
            if self._balance_factor(node.right) < 0:
                node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node

    @trace
    def insert(self, key: Any) -> None:
        self.root = self._insert(self.root, key)

    def _insert(self, node: Optional[AVLNode], key: Any) -> AVLNode:
        if not node:
            return AVLNode(key)

        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        else:
            return node  # дубликаты не вставляем

        return self._balance(node)

    @trace
    def search(self, key: Any) -> bool:
        return self._search(self.root, key)

    def _search(self, node: Optional[AVLNode], key: Any) -> bool:
        if not node:
            return False
        if key == node.key:
            return True
        if key < node.key:
            return self._search(node.left, key)
        return self._search(node.right, key)

    @trace
    def delete(self, key: Any) -> None:
        self.root = self._delete(self.root, key)

    def _delete(self, node: Optional[AVLNode], key: Any) -> Optional[AVLNode]:
        if not node:
            return None

        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:  # нода найдена
            if not node.left:
                return node.right
            if not node.right:
                return node.left
            
            min_node = node.right
            while min_node.left:
                min_node = min_node.left
            node.key = min_node.key
            node.right = self._delete(node.right, min_node.key)

        return self._balance(node) if node else None

    def __str__(self) -> str:
        return f"AVL(root={self.root.key if self.root else None})"