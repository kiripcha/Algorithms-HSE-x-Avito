# tests/test_connected_components.py
import pytest
from src.graph import find_connected_components

@pytest.mark.parametrize(
    "graph, expected",
    [
        ({}, []),  # Пустой граф
        ({1: []}, [[1]]),  # Одна изолированная вершина
        ({1: [], 2: []}, [[1], [2]]),  # Две изолированные
        ({1: [2], 2: [1]}, [[1, 2]]),  # Связная пара
        ({1: [2, 3], 2: [1, 3], 3: [1, 2]}, [[1, 2, 3]]),  # Полностью связный треугольник
        ({1: [2], 2: [1], 3: [], 4: [5], 5: [4]}, [[1, 2], [3], [4, 5]]),  # Несколько компонент
        ({'A': ['B'], 'B': ['A'], 'C': ['D', 'E'], 'D': ['C'], 'E': ['C']}, [['A', 'B'], ['C', 'D', 'E']]),  # Строковые вершины
        ({1: [1]}, [[1]]),  # Петля (игнорируется в DFS)
        ({1: [2], 2: [1, 3], 3: [2, 4], 4: [3]}, [[1, 2, 3, 4]]),  # Цепочка
        ({1: [], 2: [], 3: [], 4: []}, [[1], [2], [3], [4]]),  # Все изолированные
        ({1: [2, 3], 2: [1], 3: [1, 4], 4: [3, 5], 5: [4]}, [[1, 2, 3, 4, 5]]),  # Связный с ветвями
        ({1: [2], 2: [1], 3: [4], 4: [3], 5: []}, [[1, 2], [3, 4], [5]]),  # Смешанный
    ]
)
def test_connected_components(graph, expected):
    result = find_connected_components(graph)
    # Сортируем ожидаемое для сравнения
    expected = sorted([sorted(comp) for comp in expected], key=lambda c: c[0])
    assert result == expected


def test_large_graph():
    # Большой граф: 100 вершин, две компоненты
    graph = {}
    for i in range(1, 51):
        graph[i] = [j for j in range(1, 51) if j != i]  # Полносвязная компонента 1-50
    for i in range(51, 101):
        graph[i] = []  # Изолированные 51-100
    result = find_connected_components(graph)
    assert len(result) == 51  # 1 большая + 50 изолированных
    assert sorted(result[0]) == list(range(1, 51))


def test_non_integer_nodes():
    graph = {'apple': ['banana'], 'banana': ['apple'], 'cherry': []}
    expected = [['apple', 'banana'], ['cherry']]
    result = find_connected_components(graph)
    assert sorted([sorted(comp) for comp in result], key=lambda c: c[0]) == expected


def test_empty_lists_for_all():
    graph = {1: [], 2: [], 3: []}
    expected = [[1], [2], [3]]
    assert find_connected_components(graph) == expected


def test_graph_with_self_loop_and_isolated():
    graph = {1: [1, 2], 2: [1], 3: [3]}
    expected = [[1, 2], [3]]
    assert find_connected_components(graph) == expected


def test_unsymmetric_graph():
    # Неориентированный, но если список не симметричен (ошибка ввода), DFS все равно работает, но предполагаем симметрию
    graph = {1: [2], 2: []}  # Несимметричный, но в неориентированном должен быть симметричным
    result = find_connected_components(graph)
    assert result == [[1, 2]]  # DFS от 1 дойдет до 2, от 2 - нет, но начинаем с 1, затем 2 visited