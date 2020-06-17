import networkx as nx

def dfs(g: nx.DiGraph, key, value) -> tuple:
    root = list(g.nodes(data=True))[0]
    stack = [root]
    
    while stack:
        node = stack.pop()
        print(node)
        if value == node[1][key]:
            return node
        stack.extend([
            (el, g.nodes[el]) for el in g.adj[node[0]]
        ])
    return None