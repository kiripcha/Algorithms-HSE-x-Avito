import heapq
from typing import Dict, Hashable, Any

def dijkstra(graph: Dict[Hashable, Dict[Hashable, int]], start: Hashable) -> Dict[Hashable, int]:
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]  # (distance, node)

    while pq:
        dist, node = heapq.heappop(pq)
        if dist > distances[node]:
            continue
        for neighbor, weight in graph.get(node, {}).items():
            new_dist = dist + weight
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))

    return distances