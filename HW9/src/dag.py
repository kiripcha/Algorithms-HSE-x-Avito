from typing import Dict, Hashable, List, Tuple, Union

def detect_cycle_and_toposort(graph: Dict[Hashable, List[Hashable]]) -> Tuple[bool, Union[List[Hashable], List[Hashable]]]:
    colors = {node: 0 for node in graph}  # 0: white, 1: gray, 2: black
    toposort = []
    cycle = None

    def dfs(node, path: List[Hashable]) -> bool:
        nonlocal cycle
        colors[node] = 1  # gray
        path.append(node)
        for neighbor in graph.get(node, []):
            if colors[neighbor] == 1:  # back edge to gray
                cycle_start = path.index(neighbor)
                cycle = path[cycle_start:] + [neighbor]
                return True
            if colors[neighbor] == 0 and dfs(neighbor, path):
                return True
        path.pop()
        colors[node] = 2  # black
        toposort.append(node)
        return False

    for node in graph:
        if colors[node] == 0:
            if dfs(node, []):
                return True, cycle

    toposort.reverse()  # reverse post-order for toposort
    return False, toposort