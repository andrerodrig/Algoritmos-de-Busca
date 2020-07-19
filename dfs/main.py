import networkx as nx
from dfs import dfs

def main():
    g1 = nx.DiGraph()
    print(g1)
    g1.add_nodes_from([1,2,3,4,5])
    g1.add_edges_from([(1,2), (1,5), (2,3), (5,4)])

    g1.nodes[1]['value'] = 'a'
    g1.nodes[2]['value'] = 'operation'
    g1.nodes[3]['value'] = 'doido'
    g1.nodes[4]['value'] = 'animal'
    g1.nodes[5]['value'] = 'a10'
    result = dfs(g1, 'animal')
    print(result)
    

if __name__ == '__main__':
    main()
