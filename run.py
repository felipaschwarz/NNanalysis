from covergraph.covergraph import CoverGraph
from covergraph.helpers import fourier_matrix, inv_fourier_matrix
import string
import networkx as nx


nodes1 = list(string.ascii_lowercase)[:8]
edges1 = ['ab', 'ac', 'bd', 'be', 'bf', 'cd', 'ce', 'cf','dg', 'dh','eg', 'eh','fg', 'fh']
G1 = CoverGraph(nodes1, edges1)

print(G1.fourier_transform())

G = nx.DiGraph()
G.add_nodes_from(nodes1)
G.add_edges_from([tuple(e) for e in edges1])
print(fourier_matrix(G))

#nx.draw_circular(G, with_labels=True)
#plt.savefig("CoverGraph.png")
