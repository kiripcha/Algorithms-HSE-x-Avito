from typing import Dict, List, Hashable

def find_connected_components(graph: Dict[Hashable, List[Hashable]]) -> List[List[Hashable]]:
    visited = set()
    components = []

    def dfs(node, component):
        visited.add(node)
        component.append(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                dfs(neighbor, component)

    for node in graph:
        if node not in visited:
            component = []
            dfs(node, component)
            # Сортируем вершины в компоненте для детерминизма
            components.append(sorted(component))

    # Добавляем изолированные вершины, если они не в графе (но по задаче граф включает все вершины как ключи)
    # Предполагаем, что все вершины - ключи в словаре, даже изолированные (с пустым списком)

    # Сортируем компоненты по минимальной вершине для детерминизма
    components.sort(key=lambda c: c[0])

    return components