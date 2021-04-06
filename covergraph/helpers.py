import networkx as nx
import numpy as np

def inv_fourier_matrix(graph):
    nodes = list(graph.nodes)
    Inv_Fourier_Matrix = np.identity(graph.number_of_nodes())
    for node in nodes:
        for ancestor_node in nx.ancestors(graph, node):
            Inv_Fourier_Matrix[nodes.index(node)][nodes.index(ancestor_node)] = 1
    return Inv_Fourier_Matrix

def fourier_matrix(graph):
    Inv_Fourier_Matrix = inv_fourier_matrix(graph)
    Fourier_Matrix = np.linalg.inv(Inv_Fourier_Matrix)
    return Fourier_Matrix
