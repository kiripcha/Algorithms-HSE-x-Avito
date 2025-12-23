import pytest
from src.dag import detect_cycle_and_toposort

@pytest.mark.parametrize(
    "graph, expected_has_cycle, expected_result",
    [
        ({}, False, []),  # Пустой граф
        ({1: []}, False, [1]),  # Одна вершина, нет цикла
        ({1: [1]}, True, [1, 1]),  # Самопетля
        ({1: [2], 2: [1]}, True, [1, 2, 1]),  # Цикл из двух
        ({1: [2], 2: []}, False, [1, 2]),  # DAG цепочка
        ({1: [], 2: []}, False, [1, 2]),  # Две изолированные (порядок может варьироваться, но sort keys)
        ({1: [2, 3], 2: [4], 3: [4], 4: []}, False, [1, 3, 2, 4]),  # DAG с ветвями (возможны варианты, но проверяем is toposort)
        ({1: [2], 2: [3], 3: [1]}, True, [1, 2, 3, 1]),  # Цикл из трех
        ({1: [2], 2: [3], 3: [4], 4: [2]}, True, [2, 3, 4, 2]),  # Цикл не от корня
        ({'A': ['B'], 'B': []}, False, ['A', 'B']),  # Строки
        ({1: [2], 2: [3], 3: []}, False, [1, 2, 3]),  # Линейный DAG
        ({1: [], 2: [1]}, False, [2, 1]),  # Обратный порядок
        ({1: [1, 2], 2: [1]}, True, [1, 1]),  # Самопетля + другой цикл (может найти любой)
        ({1: [2], 2: [3], 3: [4], 4: []}, False, [1, 2, 3, 4]),  # Длинная цепь
        ({1: [2], 3: [4], 2: [], 4: []}, False, [1, 3, 2, 4]),  # Две компоненты (порядок может варьироваться)
    ]
)
def test_detect_cycle_and_toposort(graph, expected_has_cycle, expected_result):
    has_cycle, result = detect_cycle_and_toposort(graph)
    assert has_cycle == expected_has_cycle
    if has_cycle:
        # Проверяем, что цикл правильный: начинается и заканчивается одной вершиной, и есть ребра
        assert len(result) >= 2
        assert result[0] == result[-1]
        for i in range(len(result) - 1):
            assert result[i+1] in graph.get(result[i], [])
    else:
        # Проверяем, что это валидный toposort: для каждого ребра u->v, u перед v
        pos = {node: i for i, node in enumerate(result)}
        for u in graph:
            for v in graph[u]:
                assert pos[u] < pos[v]


def test_large_dag():
    graph = {i: [i+1] for i in range(100)}
    graph[100] = []
    has_cycle, result = detect_cycle_and_toposort(graph)
    assert not has_cycle
    assert result == list(range(101))


def test_large_cycle():
    graph = {i: [i+1] for i in range(100)}
    graph[100] = [0]  # цикл
    has_cycle, result = detect_cycle_and_toposort(graph)
    assert has_cycle
    assert len(result) == 101  # весь цикл


def test_disconnected_with_cycle():
    graph = {1: [2], 2: [1], 3: [4], 4: []}
    has_cycle, result = detect_cycle_and_toposort(graph)
    assert has_cycle
    assert result in [[1, 2, 1], [2, 1, 2]]  # любой из двух