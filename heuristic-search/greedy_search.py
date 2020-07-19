import heapq as h
from utils import adj_nodes


def greedy_search(g, key, value):
    root = list(g.nodes(data=True))[0]
    heap = []
    h.heappush(heap, (root[1]["valor"], root))
    visited = []

    while heap:
        node = h.heappop(heap)
        print(node)
        visited.append(node)
        if node[0] == 0:
            return f"Nó encontrado: {node}"
        else:
            if min(adj_nodes(g, node), key=lambda x: x[1]["valor"]) not in visited:
                h.heappush(
                    heap,
                    (
                        min(adj_nodes(g, node), key=lambda x: x[1]["valor"])[1][
                            "valor"
                        ],
                        min(adj_nodes(g, node), key=lambda x: x[1]["valor"]),
                    ),
                )
