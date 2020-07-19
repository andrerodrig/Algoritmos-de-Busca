def adj_nodes(graph, node):
    return [
        (n, graph.nodes(data=True)[n]) for n, datadict in graph.adj[node[1][0]].items()
    ]
