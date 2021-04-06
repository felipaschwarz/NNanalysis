import numpy as np
import networkx as nx

from covergraph.helpers import *

class CoverGraph(nx.DiGraph):
    def __init__(self, nodes=[], edges=[]):
        super().__init__()
        self.add_nodes_from(nodes)
        self.add_edges_from([tuple(e) for e in edges])

    def inv_fourier_transform(self):
        # TODO get inv_ fourier_matrix and compute transformation
        return inv_fourier_matrix(self.graph)

    def fourier_transform(self):
        # TODO get fourier_matrix and compute transformation
        return fourier_matrix(self.graph)
