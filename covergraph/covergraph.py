import numpy as np
import networkx as nx

from covergraph.helpers import *

class CoverGraph:
    def __init__(self, nodes, edges):
        self.graph = nx.DiGraph()
        self.graph.add_nodes_from(nodes)
        self.graph.add_edges_from([tuple(e) for e in edges])

    def inv_fourier_transform(self):
        # TODO get inv_ fourier_matrix and compute transformation
        nodes = list(self.graph.nodes)
        Inv_Fourier_Matrix = np.identity(self.graph.number_of_nodes())
        for node in list(self.graph.nodes):
            for ancestor_node in nx.ancestors(self.graph, node):
                Inv_Fourier_Matrix[nodes.index(node)][nodes.index(ancestor_node)] = 1
        return Inv_Fourier_Matrix

    def fourier_transform(self):
        # TODO get fourier_matrix and compute transformation
        Inv_Fourier_Matrix = self.inv_fourier_transform()
        Fourier_Matrix = np.linalg.inv(Inv_Fourier_Matrix)
        return Fourier_Matrix
