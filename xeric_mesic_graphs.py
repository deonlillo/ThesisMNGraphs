import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms import approximation

def create_clique(G, treeNodes):
   if len(treeNodes) == 1:
      G.add_node(treeNodes[0])
   for tree1 in treeNodes:
      for tree2 in treeNodes:
         if tree1 is tree2:
            continue
         G.add_edge(tree1, tree2)

def add_clique_counts(dictionary, vertices):
   for vertex in vertices:
      if vertex not in dictionary:
         dictionary[vertex] = 1
      else:
         dictionary[vertex] += 1

ves_xeric_graph = nx.Graph()
ves_xeric_cliques = {}

# VES-1-01
# Plot 1 (xeric)
ves1_1trees = [20, 4, 61, 19, 25, 21, 1, 22, 8, 38, 23, 26, 5, 41, 49, 79, 62, 81, 42, 37, 36, "U3", 35]
create_clique(ves_xeric_graph, ves1_1trees)
add_clique_counts(ves_xeric_cliques, ves1_1trees)

# VES-1-02
# Plot 1 (xeric)
ves1_2trees = [48]
create_clique(ves_xeric_graph, ves1_2trees)
add_clique_counts(ves_xeric_cliques, ves1_2trees)

# VES-1-03
# Plot 1 (xeric)
ves1_3trees = [41, 48]
create_clique(ves_xeric_graph, ves1_3trees)
add_clique_counts(ves_xeric_cliques, ves1_3trees)

# VES-1-04
# Plot 1 (xeric)
ves1_4trees = [19]
create_clique(ves_xeric_graph, ves1_4trees)
add_clique_counts(ves_xeric_cliques, ves1_4trees)
print(len(ves_xeric_graph))
print(len(ves_xeric_graph.edges))

# VES-2-01
# Plot 2 (xeric)
ves2_1trees = [11, 9, 10, 58, 6, 8, 7, 12, 4, 48]
create_clique(ves_xeric_graph, ves2_1trees)
add_clique_counts(ves_xeric_cliques, ves2_1trees)

# VES-2-02
# Plot 2 (xeric)
ves2_2trees = [9]
create_clique(ves_xeric_graph, ves2_2trees)
add_clique_counts(ves_xeric_cliques, ves2_2trees)

# VES-3-01
# Plot 3 (xeric)
ves3_1trees = [2, 1, 17, 3, 48, 14, 19, 13, 74, 52, 41, 25, 26, 16, 49, 20, 15, 32, 111, 113, 44, 46]
create_clique(ves_xeric_graph, ves3_1trees)
add_clique_counts(ves_xeric_cliques, ves3_1trees)

# VES-3-02
# Plot 3 (xeric)
ves3_2trees = [1]
create_clique(ves_xeric_graph, ves3_2trees)
add_clique_counts(ves_xeric_cliques, ves3_2trees)

# VES-3-03
# Plot 3 (xeric)
ves3_3trees = [2, 115]
create_clique(ves_xeric_graph, ves3_3trees)
add_clique_counts(ves_xeric_cliques, ves3_3trees)

# VES-3-04
# Plot 3 (xeric)
ves3_4trees = [19, 109, 82, 47]
create_clique(ves_xeric_graph, ves3_4trees)
add_clique_counts(ves_xeric_cliques, ves3_4trees)

print("\nR. VESICULOSUS GENETS - XERIC PLOTS GRAPH:")
print("\nVertex clique count:")
print(dict(sorted(ves_xeric_cliques.items(), key=lambda x:x[1], reverse=True)))
ves_xeric_graph_cc = approximation.average_clustering(ves_xeric_graph)
print("Clustering coefficient: ", ves_xeric_graph_cc)
ves_xeric_graph_dc = nx.degree_centrality(ves_xeric_graph)
print("Highest degree centrality: Node %d at %5.4f "%(max(ves_xeric_graph_dc, key=ves_xeric_graph_dc.get), max(ves_xeric_graph_dc.values())))
ves_xeric_graph_ec = nx.eigenvector_centrality(ves_xeric_graph)
print("Highest eigenvector centrality: Node %d at %5.4f "%(max(ves_xeric_graph_ec, key=ves_xeric_graph_ec.get), max(ves_xeric_graph_ec.values())))
ves_xeric_graph_bc = nx.betweenness_centrality(ves_xeric_graph)
print("Highest betweenness centrality: Node %d at %5.4f "%(max(ves_xeric_graph_bc, key=ves_xeric_graph_bc.get), max(ves_xeric_graph_bc.values())))

nx.draw(ves_xeric_graph, with_labels=True)
plt.show()

# ---------------------------------------------------------------

ves_mesic_graph = nx.Graph()
ves_mesic_cliques = {}

# VES-4-01
# Plot 4 (mesic)
ves4_1trees = [12, 19, 17, 40]
create_clique(ves_mesic_graph, ves4_1trees)
add_clique_counts(ves_mesic_cliques, ves4_1trees)

# VES-4-02
# Plot 4 (mesic)
ves4_2trees = [12, 56, 54, 47, 52, 1, 2, 92, 14, 3, 73, 16, 100, 21, 11, 37, 17, 19, 66]
create_clique(ves_mesic_graph, ves4_2trees)
add_clique_counts(ves_mesic_cliques, ves4_2trees)

# VES-4-03
# Plot 4 (mesic)
ves4_3trees = [1, 7, 3, 6]
create_clique(ves_mesic_graph, ves4_3trees)
add_clique_counts(ves_mesic_cliques, ves4_3trees)

# VES-4-04
# Plot 4 (mesic)
ves4_4trees = [100, 7]
create_clique(ves_mesic_graph, ves4_4trees)
add_clique_counts(ves_mesic_cliques, ves4_4trees)

# VES-5-01
# Plot 5 (mesic)
ves5_1trees = [5, 6, 25, 19, 21, 17, 60, 59, 18, 3, 24, "105B", 100, 10, "105B", 4]
create_clique(ves_mesic_graph, ves5_1trees)
add_clique_counts(ves_mesic_cliques, ves5_1trees)

# VES-5-02
# Plot 5 (mesic)
ves5_2trees = [10, 57, 4]
create_clique(ves_mesic_graph, ves5_2trees)
add_clique_counts(ves_mesic_cliques, ves5_2trees)

# VES-5-03
# Plot 5 (mesic)
ves5_3trees = ["105A", 24, 10]
create_clique(ves_mesic_graph, ves5_3trees)
add_clique_counts(ves_mesic_cliques, ves5_3trees)

# VES-5-04
# Plot 5 (mesic)
ves5_4trees = [107]
create_clique(ves_mesic_graph, ves5_4trees)
add_clique_counts(ves_mesic_cliques, ves5_4trees)

# VES-5-05
# Plot 5 (mesic)
ves5_5trees = [107]
create_clique(ves_mesic_graph, ves5_5trees)
add_clique_counts(ves_mesic_cliques, ves5_5trees)

# VES-5-06
# Plot 5 (mesic)
ves5_6trees = [61, 19, 108, 24, 107, 20, 100, 21, "105B", 17]
create_clique(ves_mesic_graph, ves5_6trees)
add_clique_counts(ves_mesic_cliques, ves5_6trees)

# VES-5-07
# Plot 5 (mesic)
ves5_7trees = [12, 7, 130, 20, 18, 19, 17, 100, 24, 21, 86]
create_clique(ves_mesic_graph, ves5_7trees)
add_clique_counts(ves_mesic_cliques, ves5_7trees)

# VES-6-01
# Plot 6 (mesic)
ves6_1trees = [33, 77, 79, 41, 81, 52, "U8", 59, 53, 35, 44, 1, 8, 10, 9, 37, 14, 7, 23, 117, 40, 45]
create_clique(ves_mesic_graph, ves6_1trees)
add_clique_counts(ves_mesic_cliques, ves6_1trees)

# VES-6-02
# Plot 6 (mesic)
ves6_2trees = [106, 1, 19, 2, 108, 7]
create_clique(ves_mesic_graph, ves6_2trees)
add_clique_counts(ves_mesic_cliques, ves6_2trees)

# VES-6-03
# Plot 6 (mesic)
ves6_3trees = [101, 2, 9, 37, 19]
create_clique(ves_mesic_graph, ves6_3trees)
add_clique_counts(ves_mesic_cliques, ves6_3trees)

# VES-6-04
# Plot 6 (mesic)
ves6_4trees = [1, 36, 10, 2, 7, 19, 5, 121, 33, 117, 17, 11, 56, 45]
create_clique(ves_mesic_graph, ves6_4trees)
add_clique_counts(ves_mesic_cliques, ves6_4trees)

# VES-6-05
# Plot 6 (mesic)
ves6_5trees = [19, 2]
create_clique(ves_mesic_graph, ves6_5trees)
add_clique_counts(ves_mesic_cliques, ves6_5trees)

# VES-6-06
# Plot 6 (mesic)
ves6_6trees = [45]
create_clique(ves_mesic_graph, ves6_6trees)
add_clique_counts(ves_mesic_cliques, ves6_6trees)

# VES-6-07
# Plot 6 (mesic)
ves6_7trees = [23]
create_clique(ves_mesic_graph, ves6_7trees)
add_clique_counts(ves_mesic_cliques, ves6_7trees)

print("\nR. VESICULOSUS GENETS - MESIC PLOTS GRAPH:")
print("\nVertex clique count:")
print(dict(sorted(ves_mesic_cliques.items(), key=lambda x:x[1], reverse=True)))
ves_mesic_graph_cc = approximation.average_clustering(ves_mesic_graph)
print("Clustering coefficient: ", ves_mesic_graph_cc)
ves_mesic_graph_dc = nx.degree_centrality(ves_mesic_graph)
print("Highest degree centrality: Node %d at %5.4f "%(max(ves_mesic_graph_dc, key=ves_mesic_graph_dc.get), max(ves_mesic_graph_dc.values())))
ves_mesic_graph_ec = nx.eigenvector_centrality(ves_mesic_graph)
print("Highest eigenvector centrality: Node %d at %5.4f "%(max(ves_mesic_graph_ec, key=ves_mesic_graph_ec.get), max(ves_mesic_graph_ec.values())))
ves_mesic_graph_bc = nx.betweenness_centrality(ves_mesic_graph)
print("Highest betweenness centrality: Node %d at %5.4f "%(max(ves_mesic_graph_bc, key=ves_mesic_graph_bc.get), max(ves_mesic_graph_bc.values())))

nx.draw(ves_mesic_graph, with_labels=True)
plt.show()

# ---------------------------------------------------------------

vin_xeric_graph = nx.Graph()
vin_xeric_cliques = {}
# VIN-1-01
# Plot 1 (xeric)
vin1_1trees = [1, 23, 33, 57, 26]
create_clique(vin_xeric_graph, vin1_1trees)
add_clique_counts(vin_xeric_cliques, vin1_1trees)

# VIN-1-02
# Plot 1 (xeric)
vin1_2trees = [80]
create_clique(vin_xeric_graph, vin1_2trees)
add_clique_counts(vin_xeric_cliques, vin1_2trees)

# VIN-2-01
# Plot 2 (xeric)
vin2_1trees = [6]
create_clique(vin_xeric_graph, vin2_1trees)
add_clique_counts(vin_xeric_cliques, vin2_1trees)

# VIN-2-02
# Plot 2 (xeric)
vin2_2trees = [11, 12, 10]
create_clique(vin_xeric_graph, vin2_2trees)
add_clique_counts(vin_xeric_cliques, vin2_2trees)

# VIN-2-03
# Plot 2 (xeric)
vin2_3trees = [6, 58, 9, 10, 7, 11, 13, "U1", 61, 4]
create_clique(vin_xeric_graph, vin2_3trees)
add_clique_counts(vin_xeric_cliques, vin2_3trees)

# VIN-2-04
# Plot 2 (xeric)
vin2_4trees = [6]
create_clique(vin_xeric_graph, vin2_4trees)
add_clique_counts(vin_xeric_cliques, vin2_4trees)

# VIN-3-01
# Plot 3 (xeric)
vin3_1trees = [3, 18, 1, 48, 19, 113, 51]
create_clique(vin_xeric_graph, vin3_1trees)
add_clique_counts(vin_xeric_cliques, vin3_1trees)

# VIN-3-02
# Plot 3 (xeric)
vin3_2trees = [17, 18]
create_clique(vin_xeric_graph, vin3_2trees)
add_clique_counts(vin_xeric_cliques, vin3_2trees)

# VIN-3-03
# Plot 3 (xeric)
vin3_3trees = [17]
create_clique(vin_xeric_graph, vin3_3trees)
add_clique_counts(vin_xeric_cliques, vin3_3trees)

# VIN-3-04
# Plot 3 (xeric)
vin3_4trees = [19, 2, 1, 14, 15, 113, 19, 13, 17, 118, 31, 41, 21, 25]
create_clique(vin_xeric_graph, vin3_4trees)
add_clique_counts(vin_xeric_cliques, vin3_4trees)

# VIN-3-05
# Plot 3 (xeric)
vin3_5trees = [1]
create_clique(vin_xeric_graph, vin3_5trees)
add_clique_counts(vin_xeric_cliques, vin3_5trees)

print("\nR. VINICOLOR GENETS - XERIC PLOTS GRAPH:")
print("\nVertex clique count:")
print(dict(sorted(vin_xeric_cliques.items(), key=lambda x:x[1], reverse=True)))
vin_xeric_graph_cc = approximation.average_clustering(vin_xeric_graph)
print("Clustering coefficient: ", vin_xeric_graph_cc)
vin_xeric_graph_dc = nx.degree_centrality(vin_xeric_graph)
print("Highest degree centrality: Node %d at %5.4f "%(max(vin_xeric_graph_dc, key=vin_xeric_graph_dc.get), max(vin_xeric_graph_dc.values())))
vin_xeric_graph_ec = nx.eigenvector_centrality(vin_xeric_graph)
print("Highest eigenvector centrality: Node %d at %5.4f "%(max(vin_xeric_graph_ec, key=vin_xeric_graph_ec.get), max(vin_xeric_graph_ec.values())))
vin_xeric_graph_bc = nx.betweenness_centrality(vin_xeric_graph)
print("Highest betweenness centrality: Node %d at %5.4f "%(max(vin_xeric_graph_bc, key=vin_xeric_graph_bc.get), max(vin_xeric_graph_bc.values())))

nx.draw(vin_xeric_graph, with_labels=True)
plt.show()

# ---------------------------------------------------------------

vin_mesic_graph = nx.Graph()
vin_mesic_cliques = {}

# VIN-4-01
# Plot 4 (mesic)
vin4_1trees = [59, 1, 3, 11]
create_clique(vin_mesic_graph, vin4_1trees)
add_clique_counts(vin_mesic_cliques, vin4_1trees)

# VIN-4-02
# Plot 4 (mesic)
vin4_2trees = [39, 76, 54, 7, 1, 12, 11, 14, 2, 3, 16, 17, 40, 20, 56, 15]
create_clique(vin_mesic_graph, vin4_2trees)
add_clique_counts(vin_mesic_cliques, vin4_2trees)

# VIN-5-01
# Plot 5 (mesic)
vin5_1trees = [16, 15, 17]
create_clique(vin_mesic_graph, vin5_1trees)
add_clique_counts(vin_mesic_cliques, vin5_1trees)

# VIN-5-02
# Plot 5 (mesic)
vin5_2trees = [19, 24]
create_clique(vin_mesic_graph, vin5_2trees)
add_clique_counts(vin_mesic_cliques, vin5_2trees)

# VIN-5-03
# Plot 5 (mesic)
vin5_3trees = [18]
create_clique(vin_mesic_graph, vin5_3trees)
add_clique_counts(vin_mesic_cliques, vin5_3trees)

# VIN-5-04
# Plot 5 (mesic)
vin5_4trees = [5, 6, 4]
create_clique(vin_mesic_graph, vin5_4trees)
add_clique_counts(vin_mesic_cliques, vin5_4trees)

# VIN-6-01
# Plot 6 (mesic)
vin6_1trees = [1, 3, 7, 8, 10, 37, 14, 61, 12, 117, 60, 35, 36, 38, 56, 2, 44, 41]
create_clique(vin_mesic_graph, vin6_1trees)
add_clique_counts(vin_mesic_cliques, vin6_1trees)

# VIN-6-02
# Plot 6 (mesic)
vin6_2trees = [41, 33, 35, 122, 38, 44]
create_clique(vin_mesic_graph, vin6_2trees)
add_clique_counts(vin_mesic_cliques, vin6_2trees)

# VIN-6-03
# Plot 6 (mesic)
vin6_3trees = [121, 1, 3, 2, 7, 19, 101]
create_clique(vin_mesic_graph, vin6_3trees)
add_clique_counts(vin_mesic_cliques, vin6_3trees)

# VIN-6-04
# Plot 6 (mesic)
vin6_4trees = [35, 36]
create_clique(vin_mesic_graph, vin6_4trees)
add_clique_counts(vin_mesic_cliques, vin6_4trees)

# VIN-6-05
# Plot 6 (mesic)
vin6_5trees = [19]
create_clique(vin_mesic_graph, vin6_5trees)
add_clique_counts(vin_mesic_cliques, vin6_5trees)

# VIN-6-06
# Plot 6 (mesic)
vin6_6trees = [83, 41, 35, 38, 79]
create_clique(vin_mesic_graph, vin6_6trees)
add_clique_counts(vin_mesic_cliques, vin6_6trees)

# VIN-6-07
# Plot 6 (mesic)
vin6_7trees = [35]
create_clique(vin_mesic_graph, vin6_7trees)
add_clique_counts(vin_mesic_cliques, vin6_7trees)

# VIN-6-08
# Plot 6 (mesic)
vin6_8trees = [41]
create_clique(vin_mesic_graph, vin6_8trees)
add_clique_counts(vin_mesic_cliques, vin6_8trees)

# VIN-6-09
# Plot 6 (mesic)
vin6_9trees = [51, 37]
create_clique(vin_mesic_graph, vin6_9trees)
add_clique_counts(vin_mesic_cliques, vin6_9trees)

# VIN-6-10
# Plot 6 (mesic)
vin6_10trees = [9]
create_clique(vin_mesic_graph, vin6_10trees)
add_clique_counts(vin_mesic_cliques, vin6_10trees)

print("\nR. VINICOLOR GENETS - MESIC PLOTS GRAPH:")
print("\nVertex clique count:")
print(dict(sorted(vin_mesic_cliques.items(), key=lambda x:x[1], reverse=True)))
vin_mesic_graph_cc = approximation.average_clustering(vin_mesic_graph)
print("Clustering coefficient: ", vin_mesic_graph_cc)
vin_mesic_graph_dc = nx.degree_centrality(vin_mesic_graph)
print("Highest degree centrality: Node %d at %5.4f "%(max(vin_mesic_graph_dc, key=vin_mesic_graph_dc.get), max(vin_mesic_graph_dc.values())))
vin_mesic_graph_ec = nx.eigenvector_centrality(vin_mesic_graph)
print("Highest eigenvector centrality: Node %d at %5.4f "%(max(vin_mesic_graph_ec, key=vin_mesic_graph_ec.get), max(vin_mesic_graph_ec.values())))
vin_mesic_graph_bc = nx.betweenness_centrality(vin_mesic_graph)
print("Highest betweenness centrality: Node %d at %5.4f "%(max(vin_mesic_graph_bc, key=vin_mesic_graph_bc.get), max(vin_mesic_graph_bc.values())))

nx.draw(vin_mesic_graph, with_labels=True)
plt.show()
