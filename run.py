import string
import networkx as nx

from covergraph.covergraph import CoverGraph
from covergraph.helpers import fourier_matrix, inv_fourier_matrix

from nnmodel.nnmodel import FilterVisualizer

#nx.draw_circular(G, with_labels=True)
#plt.savefig("CoverGraph.png")

# layer = 2
# filter = 265
#
# FV = FilterVisualizer(size=56, upscaling_steps=12, upscaling_factor=1.2)
# FV.visualize(layer, filter, blur=5)
#
# img = PIL.Image.open("layer_"+str(layer)+"_filter_"+str(filter)+".jpg")
# plt.figure(figsize=(7,7))
# plt.imshow(img)
