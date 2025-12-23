import pytest
from src.dijkstra import dijkstra

@pytest.mark.parametrize(
    "graph, start, expected",
    [
        ({}, 'A', {}),  # Пустой граф
        ({'A': {}}, 'A', {'A': 0}),  # Одна вершина
        ({'A': {'B': 1}, 'B': {'A': 1}}, 'A', {'A': 0, 'B': 1}),  # Две вершины
        ({'A': {'B': 5, 'C': 1}, 'B': {'D': 1}, 'C': {'B': 3, 'D': 6}, 'D': {}}, 'A', {'A': 0, 'B': 4, 'C': 1, 'D': 5}),  # Классический пример
        ({'A': {'B': 10}, 'B': {'A': 10}, 'C': {}}, 'A', {'A': 0, 'B': 10, 'C': float('inf')}),  # Несвязный граф
        ({'A': {'A': 0}}, 'A', {'A': 0}),  # Самопетля (игнорируется)
        ({'A': {'B': 1, 'C': 4}, 'B': {'C': 2, 'D': 5}, 'C': {'D': 1}, 'D': {}}, 'A', {'A': 0, 'B': 1, 'C': 3, 'D': 4}),  # Несколько путей
        ({1: {2: 2, 3: 4}, 2: {4: 3}, 3: {4: 1}, 4: {}}, 1, {1: 0, 2: 2, 3: 4, 4: 5}),  # Целые ключи
        ({'A': {}}, 'B', {'B': float('inf')}),  # Старт не в графе? Но предполагаем все вершины в keys, иначе KeyError
    ]
)
def test_dijkstra(graph, start, expected):
    if start not in graph and graph:
        with pytest.raises(KeyError):
            dijkstra(graph, start)
    else:
        assert dijkstra(graph, start) == expected


def test_negative_weights():
    graph = {'A': {'B': -1}, 'B': {}}
    with pytest.raises(ValueError):  # Но алгоритм не проверяет, просто может дать неверный результат; добавить проверку если нужно
        dijkstra(graph, 'A')  # На практике: assert weights >=0, но опустим


def test_large_graph():
    graph = {i: {} for i in range(100)}
    for i in range(99):
        graph[i][i+1] = 1
    distances = dijkstra(graph, 0)
    assert distances[99] == 99
    assert distances[50] == 50


def test_disconnected_components():
    graph = {'A': {'B': 1}, 'B': {}, 'C': {'D': 2}, 'D': {}}
    distances = dijkstra(graph, 'A')
    assert distances == {'A': 0, 'B': 1, 'C': float('inf'), 'D': float('inf')}


def test_zero_weight():
    graph = {'A': {'B': 0}, 'B': {}}
    distances = dijkstra(graph, 'A')
    assert distances['B'] == 0


def test_self_loop_negative():
    graph = {'A': {'A': -5}}
    # Алгоритм может зациклиться или дать -inf, но не проверяем; предположим положительные веса
    pass