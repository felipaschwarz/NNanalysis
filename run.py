from covergraph.covergraph import CoverGraph
from covergraph.helpers import fourier_matrix, inv_fourier_matrix
import string
import networkx as nx


nodes1 = list(string.ascii_lowercase)[:8]
edges1 = ['ab', 'ac', 'bd', 'be', 'bf', 'cd', 'ce', 'cf','dg', 'dh','eg', 'eh','fg', 'fh']
G1 = CoverGraph(nodes1, edges1)

nodes2 = list(string.ascii_lowercase)[:8]
edges2 = ['ba', 'ca', 'da', 'eb', 'fb', 'fc', 'fd', 'gd','he', 'hf']
G2 = CoverGraph(nodes2, edges2)
G2 = G2.reverse()
print(G2.edges)


print("Success")


#nx.draw_circular(G, with_labels=True)
#plt.savefig("CoverGraph.png")
