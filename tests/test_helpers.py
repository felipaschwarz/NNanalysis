import unittest
import numpy as np
import networkx as nx
import string

from helpers import *

class TestHelpers(unittest.TestCase):
    def setUp(self):
        # "Causal Signal Processing on DAGs" Fig.1
        self.G1 = nx.DiGraph()
        self.G1.add_nodes_from(list(string.ascii_lowercase)[:8])
        self.G1.add_edges_from([tuple(e) for e in ['ab', 'ac', 'bd', 'be', 'bf', 'cd', 'ce', 'cf','dg', 'dh','eg', 'eh','fg', 'fh']])

        # "Discrete Signal Processing on Meet/Join Lattices" Fig.1(a) REVERSED
        self.G2 = nx.DiGraph()
        self.G2.add_nodes_from(list(string.ascii_lowercase)[:8])
        self.G2.add_edges_from([tuple(e) for e in ['ba', 'ca', 'da', 'eb', 'fb', 'fc', 'fd', 'gd','he', 'hf']])
        self.G2 = self.G2.reverse()


    def test_inv_fourier_matrix(self):

        self.assertTrue(np.array_equal(inv_fourier_matrix(self.G1), np.array([[1., 0., 0., 0., 0., 0., 0., 0.],
                                                                        [1., 1., 0., 0., 0., 0., 0., 0.],
                                                                        [1., 0., 1., 0., 0., 0., 0., 0.],
                                                                        [1., 1., 1., 1., 0., 0., 0., 0.],
                                                                        [1., 1., 1., 0., 1., 0., 0., 0.],
                                                                        [1., 1., 1., 0., 0., 1., 0., 0.],
                                                                        [1., 1., 1., 1., 1., 1., 1., 0.],
                                                                        [1., 1., 1., 1., 1., 1., 0., 1.]])))

        self.assertTrue(np.array_equal(inv_fourier_matrix(self.G2), np.array([[1., 0., 0., 0., 0., 0., 0., 0.],
                                                                        [1., 1., 0., 0., 0., 0., 0., 0.],
                                                                        [1., 0., 1., 0., 0., 0., 0., 0.],
                                                                        [1., 0., 0., 1., 0., 0., 0., 0.],
                                                                        [1., 1., 0., 0., 1., 0., 0., 0.],
                                                                        [1., 1., 1., 1., 0., 1., 0., 0.],
                                                                        [1., 0., 0., 1., 0., 0., 1., 0.],
                                                                        [1., 1., 1., 1., 1., 1., 0., 1.]])))

    def test_fourier_matrix(self):

        self.assertTrue(np.array_equal(fourier_matrix(self.G1), np.array([[ 1.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
                                                                    [-1.,  1.,  0.,  0.,  0.,  0.,  0.,  0.],
                                                                    [-1.,  0.,  1.,  0.,  0.,  0.,  0.,  0.],
                                                                    [ 1., -1., -1.,  1.,  0.,  0.,  0.,  0.],
                                                                    [ 1., -1., -1.,  0.,  1.,  0.,  0.,  0.],
                                                                    [ 1., -1., -1.,  0.,  0.,  1.,  0.,  0.],
                                                                    [-2.,  2.,  2., -1., -1., -1.,  1.,  0.],
                                                                    [-2.,  2.,  2., -1., -1., -1.,  0.,  1.]])))

        self.assertTrue(np.array_equal(fourier_matrix(self.G2), np.array([[ 1.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
                                                                    [-1.,  1.,  0.,  0.,  0.,  0.,  0.,  0.],
                                                                    [-1.,  0.,  1.,  0.,  0.,  0.,  0.,  0.],
                                                                    [-1.,  0.,  0.,  1.,  0.,  0.,  0.,  0.],
                                                                    [ 0., -1.,  0.,  0.,  1.,  0.,  0.,  0.],
                                                                    [ 2., -1., -1., -1.,  0.,  1.,  0.,  0.],
                                                                    [ 0.,  0.,  0., -1.,  0.,  0.,  1.,  0.],
                                                                    [ 0.,  1.,  0.,  0., -1., -1.,  0.,  1.]])))


if __name__ == '__main__':
    unittest.main()
