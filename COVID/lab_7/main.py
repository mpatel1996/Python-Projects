import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

if __name__ == "__main__":
	G = np.matrix([[0,0,1,1,0,0,0,0],[0,0,1,0,1,0,0,0],[1,1,0,1,0,0,0,0],[1,0,1,0,1,1,0,0], [0,1,0,1,0,1,0,0],[0,0,0,1,1,0,0,0], [0,0,0,0,0,0,0,0], [0,0,0,0,0,1,0,0]])
	plt.subplot(121)
	K = nx.from_numpy_matrix(G)
	nx.draw(K, with_labels=0)
	nodes = ['a','b','c','d','e','f','g','h']
	plt.show()
	
