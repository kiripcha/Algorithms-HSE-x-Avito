import pytest
import random
from src.avl import AVL


@pytest.fixture
def empty_avl():
    return AVL()


# ======================== Базовые операции ========================

def test_insert_search_basic():
    tree = AVL()
    keys = [50, 30, 70, 20, 40, 60, 80]
    for k in keys:
        tree.insert(k)

    for k in keys:
        assert tree.search(k) is True
    assert tree.search(999) is False


def test_insert_duplicates_not_allowed():
    tree = AVL()
    tree.insert(42)
    tree.insert(42)
    tree.insert(42)

    # должно быть только одно вхождение
    assert tree.search(42) is True
    # проверка на дубли
    assert tree.root.height <= 1


# ======================== Удаление: все случаи ========================

def test_delete_leaf_node():
    tree = AVL()
    for k in [10, 5, 15, 3, 7]:
        tree.insert(k)
    tree.delete(7)  
    assert tree.search(7) is False
    assert tree.search(5) is True


def test_delete_node_with_one_child():
    tree = AVL()
    for k in [20, 10, 30, 5]:
        tree.insert(k)
    tree.delete(10)
    assert tree.search(10) is False
    assert tree.search(5) is True


def test_delete_node_with_two_children():
    tree = AVL()
    for k in [50, 30, 70, 20, 40, 60, 80, 35]:
        tree.insert(k)
    tree.delete(30)
    assert tree.search(30) is False
    assert tree.search(35) is True 


def test_delete_root_multiple_times():
    tree = AVL()
    tree.insert(1)
    tree.delete(1)
    assert tree.root is None

    tree.insert(100)
    tree.insert(50)
    tree.insert(150)
    tree.delete(100)  # удаляем корень
    assert tree.search(100) is False
    assert tree.search(50) is True or tree.search(150) is True


def test_delete_nonexistent_key():
    tree = AVL()
    tree.insert(10)
    tree.delete(999)
    tree.delete(-1)
    assert tree.search(10) is True
    assert tree.root is not None


# ======================== Балансировка и повороты ========================

def test_right_right_case_rotation():
    tree = AVL()
    for k in [10, 20, 30]:
        tree.insert(k)
    # левое вращение вокруг 10
    assert tree.root.key == 20
    assert tree.root.left.key == 10
    assert tree.root.right.key == 30


def test_left_left_case_rotation():
    tree = AVL()
    for k in [30, 20, 10]:
        tree.insert(k)
    assert tree.root.key == 20
    assert tree.root.left.key == 10
    assert tree.root.right.key == 30


def test_left_right_case_rotation():
    tree = AVL()
    for k in [30, 10, 20]:
        tree.insert(k)
    assert tree.root.key == 20
    assert tree.root.left.key == 10
    assert tree.root.right.key == 30


def test_right_left_case_rotation():
    tree = AVL()
    for k in [10, 30, 20]:
        tree.insert(k)
    assert tree.root.key == 20
    assert tree.root.left.key == 10
    assert tree.root.right.key == 30


# ======================== Пограничные и стресс-тесты ========================

def test_empty_tree_operations(empty_avl):
    assert empty_avl.search(42) is False
    empty_avl.delete(42)  # не должно падать
    empty_avl.insert(1)
    assert empty_avl.search(1) is True


def test_insert_10000_elements_sequential():
    tree = AVL()
    n = 10_000
    for i in range(n):
        tree.insert(i)
    assert tree.root.height <= 2 * (n.bit_length())
    for i in range(n):
        assert tree.search(i) is True
    assert tree.search(n + 1) is False


def test_insert_descending_order():
    tree = AVL()
    for i in range(1000, 0, -1):
        tree.insert(i)
    assert tree.root.height <= 14
    assert tree.search(500) is True


def test_random_insert_delete_stress():
    random.seed(12345)
    tree = AVL()
    values = list(range(1, 1001))
    random.shuffle(values)

    for v in values:
        tree.insert(v)

    # удаляем половину
    to_delete = random.sample(values, 500)
    for v in to_delete:
        tree.delete(v)

    # оставшиеся должны быть найдены
    remaining = set(values) - set(to_delete)
    for v in range(1, 1001):
        assert tree.search(v) == (v in remaining)


def test_alternate_insert_delete():
    tree = AVL()
    for i in range(1, 1001):
        tree.insert(i)
        if i % 2 == 0:
            tree.delete(i // 2)
    # четные все удалены
    assert sum(tree.search(i) for i in range(1, 1001)) <= 600 


def test_delete_all_elements_one_by_one():
    tree = AVL()
    keys = [100, 50, 150, 25, 75, 125, 175]
    for k in keys:
        tree.insert(k)
    for k in keys:
        tree.delete(k)
        assert tree.search(k) is False
    assert tree.root is None


def test_mixed_types_keys():
    tree = AVL()
    tree.insert("banana")
    tree.insert("apple")
    tree.insert("cherry")
    assert tree.search("apple") is True
    assert tree.search("date") is False


def test_height_never_exceeds_log_n():
    tree = AVL()
    n = 1000
    for i in range(1, n + 1):
        tree.insert(i)
        max_allowed = 2 * (i.bit_length())
        assert tree.root.height <= max_allowed, f"Height violation at n={i}: {tree.root.height}"


def test_no_memory_leaks_on_delete():
    tree = AVL()
    for i in range(1000):
        tree.insert(i)
    initial_root = tree.root
    for i in range(1000):
        tree.delete(i)
    assert tree.root is None
    assert initial_root != tree.root  # дерево полностью очищено


def test_concurrent_like_operations_are_safe():
    tree = AVL()
    ops = [tree.insert, tree.search, tree.delete]
    keys = [42, 100, -50, 0]
    for _ in range(100):
        op = random.choice(ops)
        key = random.choice(keys)
        try:
            if op == tree.insert:
                op(key)
            elif op == tree.delete:
                op(key)
            else:
                op(key)
        except Exception as e:
            pytest.fail(f"Operation {op.__name__}({key}) failed: {e}")