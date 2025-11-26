import pytest
from src.permutations import permutations


@pytest.mark.parametrize(
    "nums, expected_count",
    [
        ([], 1),                        # пустой список
        ([1], 1),                       # один элемент
        ([1, 1], 2),                    # все элементы одинаковые (2)
        ([1, 1, 1], 6),                 # все элементы одинаковые (3) → 3! = 6
        ([0, 1], 2),                    # два разных
        ([1, 2, 3], 6),                 # классика
        ([1, 2, 2], 6),                 # два одинаковых
        ([1, 1, 2, 2], 24),             # два по два
        ([1, 2, 3, 4], 24),             # 4!
        (list(range(5)), 120),          # 5!
        ([-1, 0, 1], 6),                # отрицательные и ноль
        ([100, 200, 300], 6),           # большие числа
    ],
)
def test_permutations_count_and_composition(nums, expected_count):
    result = permutations(nums)
    assert len(result) == expected_count
    # перестановка должна содержать ровно те же элементы
    for perm in result:
        assert sorted(perm) == sorted(nums)


def test_exact_output_order_independent():
    """проверяем точный набор перестановок"""
    expected = [
        [1, 2, 3],
        [1, 3, 2],
        [2, 1, 3],
        [2, 3, 1],
        [3, 1, 2],
        [3, 2, 1],
    ]
    assert sorted(permutations([1, 2, 3])) == sorted(expected)


def test_empty_input():
    assert permutations([]) == [[]]


def test_single_element_various_types():
    assert permutations([42]) == [[42]]
    assert permutations(["a"]) == [["a"]]
    assert permutations([None]) == [[None]]
    assert permutations([False]) == [[False]]


def test_all_identical_elements():
    assert len(permutations([7, 7, 7, 7])) == 24  # 4! = 24
    assert len(permutations([0] * 6)) == 720     # 6! = 720
    result = permutations([5, 5])
    assert result == [[5, 5], [5, 5]]


def test_with_duplicates_correct_composition():
    result = permutations([1, 1, 2])
    assert len(result) == 6
    assert all(sorted(p) == [1, 1, 2] for p in result)
    # уникальных по значению — 3, но всего перестановок — 6
    unique_tuples = set(tuple(p) for p in result)
    assert unique_tuples == {(1, 1, 2), (1, 2, 1), (2, 1, 1)}


def test_mixed_types():
    """поддержка разных типов"""
    result = permutations(["x", 42, None])
    assert len(result) == 6
    assert all(sorted(p, key=str) == sorted(["x", 42, None], key=str) for p in result)


def test_large_numerical_range():
    nums = [-100, -50, 0, 50, 100]
    result = permutations(nums)
    assert len(result) == 120  # 5!
    # проверяем, что нет потери элементов
    for perm in result:
        assert set(perm) == set(nums)


def test_no_side_effects():
    """убеждаемся, что входной список не мутируется"""
    original = [1, 2, 3]
    frozen = original.copy()
    permutations(original)
    assert original == frozen  # не изменился


def test_idempotency():
    """два вызова с одним и тем же входом дают одинаковый результат"""
    nums = [1, 2, 3]
    r1 = permutations(nums)
    r2 = permutations(nums)
    assert sorted(r1) == sorted(r2)


def test_deterministic_output():
    """результат всегда один и тот же при одинаковом входе"""
    nums = [3, 1, 2]
    expected_first = permutations(nums)[0]
    # при многократном запуске первая перестановка всегда одинаковая
    assert permutations(nums)[0] == expected_first