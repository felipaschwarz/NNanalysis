import numpy as np
import networkx as nx

from covergraph.helpers import *

class CoverGraph(nx.DiGraph):
    def __init__(self, nodes=[], edges=[]):
        super().__init__()
        self.add_nodes_from(nodes)
        self.add_edges_from([tuple(e) for e in edges])

    def inv_fourier_transform(self, signals):
        inv_F = inv_fourier_matrix(self)
        inv_fourier_signals = inv_F @ signals
        return inv_fourier_signals

    def fourier_transform(self, signals):
        F = fourier_matrix(self)
        fourier_signals = F @ signals
        return fourier_signals

    def set_node_attributes_from(self, signals, name):
        nx.set_node_attributes(self, dict(zip(self.nodes, signals)), name)
        return
