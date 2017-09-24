import matplotlib.pyplot as plt
import networkx as nx
import pickle
import random

exes = pickle.load(open("exes", "rb"))
dem = pickle.load(open("dem", "rb"))

ind = {}
cur = 0
G=nx.Graph()
for i in range(len(exes)):
	x = exes[i]
	if (x[0][0] not in ind.keys()):
		cur += 1
		ind[x[0][0]] = (cur, dem[i][0])
		c=''
		if ('Executive' in dem[i][0]):
			print(x[0][0])
			c = 'red'
		else:
			c = 'c'
		G.add_node(cur, color=c)
	if (x[0][1] not in ind.keys()):
		cur += 1
		ind[x[0][1]] = (cur, dem[i][1])
		c=''
		if ('Executive' in dem[i][1]):
			print(x[0][1])
			c = 'red'
		else:
			c = 'c'
		G.add_node(cur, color=c)

l = cur


for exe in exes:
	i = ind[exe[0][0]][0]
	j = ind[exe[0][1]][0]
	G.add_edge(i, j, weight=exe[1][5])


for exe in exes:
	i = ind[exe[0][0]][0]
	j = ind[exe[0][1]][0]
	G[i][j]["weight"]=exe[1][0]



nodecolor = [ d['color'] for (u,d) in G.nodes(data=True)]

pos = nx.random_layout(G)

edgewidth = [ d['weight'] * 7 for (u,v,d) in G.edges(data=True)]


nx.draw_networkx_nodes(G, pos, node_size=80, node_color=nodecolor)
nx.draw_networkx_edges(G, pos, width=edgewidth, color='g', alpha=1)
plt.show()