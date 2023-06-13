import networkx as nx
import matplotlib.pyplot as plt
from netgraph import Graph, InteractiveGraph, EditableGraph
from networkx.algorithms import approximation

def create_clique(G, treeNodes):
   if len(treeNodes) == 1:
      G.add_node(treeNodes[0])
   for tree1 in treeNodes:
      for tree2 in treeNodes:
         if tree1 is tree2:
            continue
         G.add_edge(tree1, tree2)

def calc_mean_node_degree(G):
   total_node_degree = 0
   for node in G.nodes:
      total_node_degree += G.degree(node)
   mean_node_degree = total_node_degree / len(G.nodes)
   return mean_node_degree

G = nx.Graph()
vertices = [1, 2, 3, 4, 5, 6, 7]
create_clique(G, vertices)

print("Total nodes:", len(G.nodes))
print("Total Links:", len(G.edges))
G_aspt = nx.average_shortest_path_length(G)
print("Mean Path Length:", G_aspt)
G_mnd = calc_mean_node_degree(G)
print("Mean Node Degree:", G_mnd)
G_cc = nx.average_clustering(G)
print("Clustering coefficient:", G_cc)

G_dc = nx.degree_centrality(G)
print("Highest degree centrality: Node %d at %5.4f "%(max(G_dc, key=G_dc.get), max(G_dc.values())))
G_ec = nx.eigenvector_centrality(G)
print("Highest eigenvector centrality: Node %d at %5.4f "%(max(G_ec, key=G_ec.get), max(G_ec.values())))
G_bc = nx.betweenness_centrality(G)
print("Highest betweenness centrality: Node %d at %5.4f "%(max(G_bc, key=G_bc.get), max(G_bc.values())))

nx.draw(G, pos=nx.kamada_kawai_layout(G), node_size=1000, with_labels=True)
plt.show()





G_2 = nx.Graph()
G_2.add_node(1)
G_2.add_node(2)
G_2.add_node(3)
G_2.add_node(4)
G_2.add_node(5)
G_2.add_node(6)
G_2.add_edge(2, 3)
G_2.add_edge(3, 4)
G_2.add_edge(2, 4)
G_2.add_edge(1, 2)
G_2.add_edge(4, 5)
G_2.add_edge(1, 5)
G_2.add_edge(5, 6)

print("\nTotal nodes:", len(G_2.nodes))
print("Total Links:", len(G_2.edges))
G_2_aspt = nx.average_shortest_path_length(G_2)
print("Mean Path Length:", G_2_aspt)
G_2_mnd = calc_mean_node_degree(G_2)
print("Mean Node Degree:", G_2_mnd)
G_2_cc = nx.average_clustering(G_2)
print("Clustering coefficient:", G_2_cc)

G_2_dc = nx.degree_centrality(G_2)
print("Highest degree centrality: Node %d at %5.4f "%(max(G_2_dc, key=G_2_dc.get), max(G_2_dc.values())))
G_2_ec = nx.eigenvector_centrality(G_2)
print("Highest eigenvector centrality: Node %d at %5.4f "%(max(G_2_ec, key=G_2_ec.get), max(G_2_ec.values())))
G_2_bc = nx.betweenness_centrality(G_2)
print("Highest betweenness centrality: Node %d at %5.4f "%(max(G_2_bc, key=G_2_bc.get), max(G_2_bc.values())))

nx.draw(G_2, pos=nx.kamada_kawai_layout(G_2), node_size=1000, with_labels=True)
plt.show()






G_3 = nx.Graph()
G_3.add_node(1)
G_3.add_node(2)
G_3.add_node(3)
G_3.add_node(4)
G_3.add_node(5)
G_3.add_node(6)
G_3.add_node(7)
G_3.add_node(8)
G_3.add_node(9)
G_3.add_node(10)
G_3.add_node(11)
G_3.add_node(12)
G_3.add_node(13)
G_3.add_node(14)
G_3.add_node(15)
G_3.add_node(16)
G_3.add_node(17)
G_3.add_node(18)


G_3.add_edge(1, 2)
G_3.add_edge(2, 3)
G_3.add_edge(2, 4)
G_3.add_edge(4, 5)
G_3.add_edge(5, 6)
G_3.add_edge(4, 6)
G_3.add_edge(6, 7)
G_3.add_edge(3, 7)
G_3.add_edge(3, 6)

G_3.add_edge(6, 8)
G_3.add_edge(8, 9)
G_3.add_edge(9, 10)


G_3.add_edge(8, 11)
G_3.add_edge(11, 12)
G_3.add_edge(11, 13)
G_3.add_edge(11, 14)
G_3.add_edge(11, 15)
G_3.add_edge(11, 16)

G_3.add_edge(8, 17)
G_3.add_edge(17, 18)




G_3_dc = nx.degree_centrality(G_3)
print("\nHighest degree centrality: Node %d at %5.4f "%(max(G_3_dc, key=G_3_dc.get), max(G_3_dc.values())))
G_3_ec = nx.eigenvector_centrality(G_3)
print("Highest eigenvector centrality: Node %d at %5.4f "%(max(G_3_ec, key=G_3_ec.get), max(G_3_ec.values())))
G_3_bc = nx.betweenness_centrality(G_3)
print("Highest betweenness centrality: Node %d at %5.4f "%(max(G_3_bc, key=G_3_bc.get), max(G_3_bc.values())))

nx.draw(G_3, pos=nx.kamada_kawai_layout(G_3), node_size=1000, with_labels=True)
plt.show()