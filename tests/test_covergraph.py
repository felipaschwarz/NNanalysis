import unittest
import numpy as np
import string

import networkx as nx

from covergraph import CoverGraph

class TestCoverGraph(unittest.TestCase):
    def setUp(self):

        # "Discrete Signal Processing on Meet/Join Lattices" Fig.1(a) REVERSED
        self.nodes2 = list(string.ascii_lowercase)[:8]
        self.edges2 = ['ba', 'ca', 'da', 'eb', 'fb', 'fc', 'fd', 'gd','he', 'hf']
        self.G2 = CoverGraph(self.nodes2, self.edges2)
        self.G2 = self.G2.reverse()
        self.signals2 = [2, 1, 2, 5, 1, 8, 5, 8]
        self.fourier_signals2 = [2, -1, 0, 3, 0, 4, 0, 0]

        self.nodes3 = list(string.ascii_lowercase)[:10]
        self.edges3 = []
        self.G3 = CoverGraph(self.nodes3, self.edges3)
        self.signals3 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.fourier_signals3 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

        self.nodes4 = list(string.ascii_lowercase)[:3]
        self.edges4 = ['ac', 'bc']
        self.G4 = CoverGraph(self.nodes4, self.edges4)
        self.signals4 = [1, 2, 3]
        self.fourier_signals4 = [1, 2, 0]

        self.nodes5 = list(string.ascii_lowercase)[:6]
        self.edges5 = ['ae', 'af', 'bd', 'cd', 'df']
        self.G5 = CoverGraph(self.nodes5, self.edges5)
        self.signals5 = [-1, 0, -2, 1, 4, 2]
        self.fourier_signals5 = [-1, 0, -2, 3, 5, 2]

        self.nodes6 = list(string.ascii_lowercase)[:1]
        self.edges6 = []
        self.G6 = CoverGraph(self.nodes6, self.edges6)
        self.signals6 = [3]
        self.fourier_signals6 = [3]


    def test_inv_fourier_transform(self):

        self.assertTrue(np.array_equal(self.G2.inv_fourier_transform(self.fourier_signals2), np.array([2, 1, 2, 5, 1, 8, 5, 8])))

        self.assertTrue(np.array_equal(self.G3.inv_fourier_transform(self.fourier_signals3), np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])))

        self.assertTrue(np.array_equal(self.G4.inv_fourier_transform(self.fourier_signals4), np.array([1, 2, 3])))

        self.assertTrue(np.array_equal(self.G5.inv_fourier_transform(self.fourier_signals5), np.array([-1, 0, -2, 1, 4, 2])))

        self.assertTrue(np.array_equal(self.G6.inv_fourier_transform(self.fourier_signals6), np.array([3])))


    def test_fourier_transform(self):

        self.assertTrue(np.array_equal(self.G2.fourier_transform(self.signals2), np.array([2, -1, 0, 3, 0, 4, 0, 0])))

        self.assertTrue(np.array_equal(self.G3.fourier_transform(self.signals3), np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])))

        self.assertTrue(np.array_equal(self.G4.fourier_transform(self.signals4), np.array([1, 2, 0])))

        self.assertTrue(np.array_equal(self.G5.fourier_transform(self.signals5), np.array([-1, 0, -2, 3, 5, 2])))

        self.assertTrue(np.array_equal(self.G6.fourier_transform(self.signals6), np.array([3])))


    def test_set_node_attributes_from(self):

        self.G2.set_node_attributes_from([1, 2, 3, 4, 5, 6, 7, 8], 'testsignal')
        self.assertEqual(nx.get_node_attributes(self.G2,'testsignal'), dict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}))
        self.G2.set_node_attributes_from([8, 8, 8, 8, 8, 8, 8, 8], 'testsignal')
        self.assertEqual(nx.get_node_attributes(self.G2,'testsignal'), dict({'a': 8, 'b': 8, 'c': 8, 'd': 8, 'e': 8, 'f': 8, 'g': 8, 'h': 8}))


if __name__ == '__main__':
    unittest.main()
