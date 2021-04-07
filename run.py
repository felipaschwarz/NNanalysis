from covergraph.covergraph import CoverGraph
from covergraph.helpers import fourier_matrix, inv_fourier_matrix
import string
import networkx as nx

nodes2 = list(string.ascii_lowercase)[:8]
signals2 = [2, 1, 2, 5, 1, 8, 5, 8]
edges2 = ['ba', 'ca', 'da', 'eb', 'fb', 'fc', 'fd', 'gd','he', 'hf']
G2 = CoverGraph(nodes2, edges2)
nx.set_node_attributes(G2, dict(zip(nodes2, signals2)), 'signal')
G2 = G2.reverse()

f_signals = G2.fourier_transform(signals2)
G2.set_node_attributes_from(f_signals, 'fourier')

inv_f_signals = G2.inv_fourier_transform(f_signals)
G2.set_node_attributes_from(inv_f_signals, 'inv_fourier')


print(nx.get_node_attributes(G2,'signal'))

print(nx.get_node_attributes(G2,'fourier'))

print(nx.get_node_attributes(G2,'inv_fourier'))


#nx.draw_circular(G, with_labels=True)
#plt.savefig("CoverGraph.png")
