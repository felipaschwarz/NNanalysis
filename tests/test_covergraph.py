import unittest
import numpy as np
import string

from covergraph.covergraph import CoverGraph

class TestCoverGraph(unittest.TestCase):
    def setUp(self):
        # "Causal Signal Processing on DAGs" Fig.1
        self.nodes1 = list(string.ascii_lowercase)[:8]
        self.edges1 = ['ab', 'ac', 'bd', 'be', 'bf', 'cd', 'ce', 'cf','dg', 'dh','eg', 'eh','fg', 'fh']
        self.G1 = CoverGraph(self.nodes1, self.edges1)

        # "Discrete Signal Processing on Meet/Join Lattices" Fig.1(a) REVERSED
        self.nodes2 = list(string.ascii_lowercase)[:8]
        self.edges2 = ['ba', 'ca', 'da', 'eb', 'fb', 'fc', 'fd', 'gd','he', 'hf']
        self.G2 = CoverGraph(self.nodes2, self.edges2)
        #self.G2 = self.G2.reverse()

    def test_inv_fourier_transform(self):

        self.assertTrue(np.array_equal(self.G1.inv_fourier_transform(), np.array([[1., 0., 0., 0., 0., 0., 0., 0.],
                                                                                [1., 1., 0., 0., 0., 0., 0., 0.],
                                                                                [1., 0., 1., 0., 0., 0., 0., 0.],
                                                                                [1., 1., 1., 1., 0., 0., 0., 0.],
                                                                                [1., 1., 1., 0., 1., 0., 0., 0.],
                                                                                [1., 1., 1., 0., 0., 1., 0., 0.],
                                                                                [1., 1., 1., 1., 1., 1., 1., 0.],
                                                                                [1., 1., 1., 1., 1., 1., 0., 1.]])))

        self.assertTrue(np.array_equal(self.G2.inv_fourier_transform(), np.array([[1., 0., 0., 0., 0., 0., 0., 0.],
                                                                                [1., 1., 0., 0., 0., 0., 0., 0.],
                                                                                [1., 0., 1., 0., 0., 0., 0., 0.],
                                                                                [1., 0., 0., 1., 0., 0., 0., 0.],
                                                                                [1., 1., 0., 0., 1., 0., 0., 0.],
                                                                                [1., 1., 1., 1., 0., 1., 0., 0.],
                                                                                [1., 0., 0., 1., 0., 0., 1., 0.],
                                                                                [1., 1., 1., 1., 1., 1., 0., 1.]])))

    def test_fourier_transform(self):

        self.assertTrue(np.array_equal(self.G1.fourier_transform(), np.array([[ 1.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
                                                                            [-1.,  1.,  0.,  0.,  0.,  0.,  0.,  0.],
                                                                            [-1.,  0.,  1.,  0.,  0.,  0.,  0.,  0.],
                                                                            [ 1., -1., -1.,  1.,  0.,  0.,  0.,  0.],
                                                                            [ 1., -1., -1.,  0.,  1.,  0.,  0.,  0.],
                                                                            [ 1., -1., -1.,  0.,  0.,  1.,  0.,  0.],
                                                                            [-2.,  2.,  2., -1., -1., -1.,  1.,  0.],
                                                                            [-2.,  2.,  2., -1., -1., -1.,  0.,  1.]])))

        self.assertTrue(np.array_equal(self.G2.fourier_transform(), np.array([[ 1.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
                                                                            [-1.,  1.,  0.,  0.,  0.,  0.,  0.,  0.],
                                                                            [-1.,  0.,  1.,  0.,  0.,  0.,  0.,  0.],
                                                                            [-1.,  0.,  0.,  1.,  0.,  0.,  0.,  0.],
                                                                            [ 0., -1.,  0.,  0.,  1.,  0.,  0.,  0.],
                                                                            [ 2., -1., -1., -1.,  0.,  1.,  0.,  0.],
                                                                            [ 0.,  0.,  0., -1.,  0.,  0.,  1.,  0.],
                                                                            [ 0.,  1.,  0.,  0., -1., -1.,  0.,  1.]])))


if __name__ == '__main__':
    unittest.main()
