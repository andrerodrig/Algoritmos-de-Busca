import networkx as nx
from collections import deque


def bfs(g: nx.DiGraph, key, value) -> tuple:
    root = list(g.nodes(data=True))[0]
    queue = deque()
    queue.append(root)
    viewed = []
    
    while queue:
        node = queue.popleft() # 1st element of the queue
        print(node)
        viewed.append(node)
        if value == node[1][key]:
            return f' Nó encontrado: {node}'
        queue.extend([
            (el, g.nodes[el]) for el in g.adj[node[0]]
            if (el, g.nodes[el]) not in viewed
            and (el, g.nodes[el]) not in queue
        ])
    return None