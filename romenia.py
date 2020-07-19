import networkx as nx
import matplotlib.pyplot as plt
from cidades import CIDADES


def romenia_gen():
    Romenia = nx.Graph()
    Romenia.add_nodes_from(range(1, 21))

    for i in range(len(Romenia.nodes)):
        Romenia.nodes[i + 1]["cidade"] = CIDADES[i]
        Romenia.nodes[i + 1]["valor"] = None

    Romenia.add_weighted_edges_from(
        [
            (1, 2, 75),
            (1, 4, 140),
            (1, 5, 118),
            (2, 3, 71),
            (3, 4, 151),
            (4, 9, 99),
            (4, 10, 80),
            (5, 6, 111),
            (6, 7, 70),
            (7, 8, 75),
            (8, 11, 120),
            (9, 13, 211),
            (10, 11, 146),
            (10, 12, 97),
            (12, 13, 101),
            (13, 14, 90),
            (13, 15, 85),
            (15, 16, 98),
            (15, 18, 142),
            (16, 17, 86),
            (18, 19, 92),
            (19, 20, 87),
        ]
    )
    return Romenia


def add_heuristic(Romenia):
    values = (
        366,
        0,
        160,
        242,
        161,
        176,
        77,
        151,
        226,
        224,
        241,
        234,
        380,
        100,
        193,
        253,
        329,
        80,
        199,
        374,
    )
    ordered = sorted(Romenia.nodes(data=True), key=lambda elem: elem[1]["cidade"])
    return ordered


def romenia_plot(Romenia):
    plt.figure(figsize=(15, 10))

    pos = nx.spring_layout(Romenia)

    nx.draw(Romenia, pos, with_labels=True)
    nx.draw_networkx_edge_labels(
        Romenia,
        pos,
        edge_labels={
            (1, 2): Romenia[1][2]["weight"],
            (1, 4): Romenia[1][4]["weight"],
            (1, 5): Romenia[1][5]["weight"],
            (2, 3): Romenia[2][3]["weight"],
            (3, 4): Romenia[3][4]["weight"],
            (4, 9): Romenia[4][9]["weight"],
            (4, 10): Romenia[4][10]["weight"],
            (5, 6): Romenia[5][6]["weight"],
            (6, 7): Romenia[6][7]["weight"],
            (7, 8): Romenia[7][8]["weight"],
            (8, 11): Romenia[8][11]["weight"],
            (9, 13): Romenia[9][13]["weight"],
            (10, 11): Romenia[10][11]["weight"],
            (10, 12): Romenia[10][12]["weight"],
            (12, 13): Romenia[12][13]["weight"],
            (13, 14): Romenia[13][14]["weight"],
            (13, 15): Romenia[13][15]["weight"],
            (15, 16): Romenia[15][16]["weight"],
            (15, 18): Romenia[15][18]["weight"],
            (16, 17): Romenia[16][17]["weight"],
            (18, 19): Romenia[18][19]["weight"],
            (19, 20): Romenia[19][20]["weight"],
        },
    )

    plt.show()
