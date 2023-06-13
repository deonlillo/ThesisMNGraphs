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

def add_clique_counts(dictionary, vertices):
   for vertex in vertices:
      if vertex not in dictionary:
         dictionary[vertex] = 1
      else:
         dictionary[vertex] += 1

def calc_mean_node_degree(G):
   total_node_degree = 0
   for node in G.nodes:
      total_node_degree += G.degree(node)
   mean_node_degree = total_node_degree / len(G.nodes)
   return mean_node_degree


# COHORT 1
co1G = nx.Graph()
co1G_cliques = {}

# VES-10
ves10trees = [40]
create_clique(co1G, ves10trees)
add_clique_counts(co1G_cliques, ves10trees)

# VIN-03
vin3trees = [40]
create_clique(co1G, vin3trees)
add_clique_counts(co1G_cliques, vin3trees)

print("\nCOHORT 1 GRAPH:")
print("\nVertex clique count:")
print(dict(sorted(co1G_cliques.items(), key=lambda x:x[1], reverse=True)))
co1G_cc = approximation.average_clustering(co1G)
print("Clustering coefficient: ", co1G_cc)
co1G_dc = nx.degree_centrality(co1G)
print("Highest degree centrality: Node %d at %5.4f "%(max(co1G_dc, key=co1G_dc.get), max(co1G_dc.values())))
co1G_ec = nx.eigenvector_centrality(co1G)
print("Highest eigenvector centrality: Node %d at %5.4f "%(max(co1G_ec, key=co1G_ec.get), max(co1G_ec.values())))
co1G_bc = nx.betweenness_centrality(co1G)
print("Highest betweenness centrality: Node %d at %5.4f "%(max(co1G_bc, key=co1G_bc.get), max(co1G_bc.values())))
co1G_mnd = calc_mean_node_degree(co1G)
print("Mean Node Degree: ", co1G_mnd)

nx.draw(co1G, with_labels=True)
plt.show()

# COHORT 2
co2G = nx.Graph()
co2G_cliques = {}

# VES-01
ves1trees = [3, 4, 50, 53, 54]
create_clique(co2G, ves1trees)
add_clique_counts(co2G_cliques, ves1trees)

# VES-02
ves2trees = [3, 4]
create_clique(co2G, ves2trees)
add_clique_counts(co2G_cliques, ves2trees)

# VES-03
ves3trees = [62]
create_clique(co2G, ves3trees)
add_clique_counts(co2G_cliques, ves3trees)

# VES-06
ves6trees = [35, 44, 50, 55, 59, 88]
create_clique(co2G, ves6trees)
add_clique_counts(co2G_cliques, ves6trees)

# VES-07
ves7trees = [7, 10, 11]
create_clique(co2G, ves7trees)
add_clique_counts(co2G_cliques, ves7trees)

# VES-09
ves9trees = [11, 13, 27]
create_clique(co2G, ves9trees)
add_clique_counts(co2G_cliques, ves9trees)

# VES-10
ves10trees = [30]
create_clique(co2G, ves10trees)
add_clique_counts(co2G_cliques, ves10trees)

# VES-11
ves11trees = [79]
create_clique(co2G, ves11trees)
add_clique_counts(co2G_cliques, ves11trees)

# VES-13
ves13trees = [11, 81]
create_clique(co2G, ves13trees)
add_clique_counts(co2G_cliques, ves13trees)

# VIN-01
vin1trees = [69]
create_clique(co2G, vin1trees)
add_clique_counts(co2G_cliques, vin1trees)

# VIN-02
vin2trees = [14, 15]
create_clique(co2G, vin2trees)
add_clique_counts(co2G_cliques, vin2trees)

# VIN-03
vin3trees = [41]
create_clique(co2G, vin3trees)
add_clique_counts(co2G_cliques, vin3trees)

# VIN-04
vin4trees = [27, 31]
create_clique(co2G, vin4trees)
add_clique_counts(co2G_cliques, vin4trees)

# VIN-05
vin5trees = [50, 54, 55, 56]
create_clique(co2G, vin5trees)
add_clique_counts(co2G_cliques, vin5trees)

# VIN-06
vin6trees = [30]
create_clique(co2G, vin6trees)
add_clique_counts(co2G_cliques, vin6trees)

# VIN-09
vin9trees = [3, 4]
create_clique(co2G, vin9trees)
add_clique_counts(co2G_cliques, vin9trees)

# VIN-10
vin10trees = [7]
create_clique(co2G, vin10trees)
add_clique_counts(co2G_cliques, vin10trees)

# VIN-12
vin12trees = [3, 4]
create_clique(co2G, vin12trees)
add_clique_counts(co2G_cliques, vin12trees)

print("\nCOHORT 2 GRAPH:")
print("\nVertex clique count:")
print(dict(sorted(co2G_cliques.items(), key=lambda x:x[1], reverse=True)))
co2G_cc = approximation.average_clustering(co2G)
print("Clustering coefficient: ", co2G_cc)
co2G_dc = nx.degree_centrality(co2G)
print("Highest degree centrality: Node %d at %5.4f "%(max(co2G_dc, key=co2G_dc.get), max(co2G_dc.values())))
co2G_ec = nx.eigenvector_centrality(co2G)
print("Highest eigenvector centrality: Node %d at %5.4f "%(max(co2G_ec, key=co2G_ec.get), max(co2G_ec.values())))
co2G_bc = nx.betweenness_centrality(co2G)
print("Highest betweenness centrality: Node %d at %5.4f "%(max(co2G_bc, key=co2G_bc.get), max(co2G_bc.values())))
co2G_mnd = calc_mean_node_degree(co2G)
print("Mean Node Degree: ", co2G_mnd)

nx.draw(co2G, with_labels=True)
plt.show()

# COHORT 3
co3G = nx.Graph()
co3G_cliques = {}

# VES-01
ves1trees = [5, 6, 9, 17, 18, 20, 49, 51, 52, 87]
create_clique(co3G, ves1trees)
add_clique_counts(co3G_cliques, ves1trees)

# VES-02
ves2trees = [9, 52]
create_clique(co3G, ves2trees)
add_clique_counts(co3G_cliques, ves2trees)

# VES-03
ves3trees = [9, 49, 87]
create_clique(co3G, ves3trees)
add_clique_counts(co3G_cliques, ves3trees)

# VES-04
ves4trees = [87]
create_clique(co3G, ves4trees)
add_clique_counts(co3G_cliques, ves4trees)

# VES-05
ves5trees = [87]
create_clique(co3G, ves5trees)
add_clique_counts(co3G_cliques, ves5trees)

# VES-06
ves6trees = [2, 18, 19, 20, 49, 52, 87]
create_clique(co3G, ves6trees)
add_clique_counts(co3G_cliques, ves6trees)

# VES-07
ves7trees = [6, 8, 9, 12, 17, 18, 19, 20, 74, 75]
create_clique(co3G, ves7trees)
add_clique_counts(co3G_cliques, ves7trees)

# VES-08
ves8trees = [52]
create_clique(co3G, ves8trees)
add_clique_counts(co3G_cliques, ves8trees)

# VES-09
ves9trees = [12, 21, 91]
create_clique(co3G, ves9trees)
add_clique_counts(co3G_cliques, ves9trees)

# VES-10
ves10trees = [9, 20, 21]
create_clique(co3G, ves10trees)
add_clique_counts(co3G_cliques, ves10trees)

# VES-12
ves12trees = [9]
create_clique(co3G, ves12trees)
add_clique_counts(co3G_cliques, ves12trees)

# VES-13
ves13trees = [9]
create_clique(co3G, ves13trees)
add_clique_counts(co3G_cliques, ves13trees)

# VIN-01
vin1trees = [6, 9, 12]
create_clique(co3G, vin1trees)
add_clique_counts(co3G_cliques, vin1trees)

# VIN-02
vin2trees = [9]
create_clique(co3G, vin2trees)
add_clique_counts(co3G_cliques, vin2trees)

# VIN-04
vin4trees = [12]
create_clique(co3G, vin4trees)
add_clique_counts(co3G_cliques, vin4trees)

# VIN-05
vin5trees = [49, 87, 89]
create_clique(co3G, vin5trees)
add_clique_counts(co3G_cliques, vin5trees)

# VIN-08
vin8trees = [18, 21]
create_clique(co3G, vin8trees)
add_clique_counts(co3G_cliques, vin8trees)

# VIN-09
vin9trees = [87]
create_clique(co3G, vin9trees)
add_clique_counts(co3G_cliques, vin9trees)

# VIN-11
vin11trees = [17]
create_clique(co3G, vin11trees)
add_clique_counts(co3G_cliques, vin11trees)

# VIN-12
vin12trees = [5, 6, 9]
create_clique(co3G, vin12trees)
add_clique_counts(co3G_cliques, vin12trees)

print("\nCOHORT 3 GRAPH:")
print("\nVertex clique count:")
print(dict(sorted(co3G_cliques.items(), key=lambda x:x[1], reverse=True)))
co3G_cc = approximation.average_clustering(co3G)
print("Clustering coefficient: ", co3G_cc)
co3G_dc = nx.degree_centrality(co3G)
print("Highest degree centrality: Node %d at %5.4f "%(max(co3G_dc, key=co3G_dc.get), max(co3G_dc.values())))
co3G_ec = nx.eigenvector_centrality(co3G)
print("Highest eigenvector centrality: Node %d at %5.4f "%(max(co3G_ec, key=co3G_ec.get), max(co3G_ec.values())))
co3G_bc = nx.betweenness_centrality(co3G)
print("Highest betweenness centrality: Node %d at %5.4f "%(max(co3G_bc, key=co3G_bc.get), max(co3G_bc.values())))
co3G_mnd = calc_mean_node_degree(co3G)
print("Mean Node Degree: ", co3G_mnd)

nx.draw(co3G, with_labels=True)
plt.show()

# COHORT 4
co4G = nx.Graph()
co4G_cliques = {}

# VES-01
ves1trees = [16, 23, 64, 86]
create_clique(co4G, ves1trees)
add_clique_counts(co4G_cliques, ves1trees)

# VES-02
ves2trees = [24, 83, 90]
create_clique(co4G, ves2trees)
add_clique_counts(co4G_cliques, ves2trees)

# VES-03
ves3trees = [23, 85]
create_clique(co4G, ves3trees)
add_clique_counts(co4G_cliques, ves3trees)

# VES-06
ves6trees = [16, 23, 83, 85, 86]
create_clique(co4G, ves6trees)
add_clique_counts(co4G_cliques, ves6trees)

# VES-07
ves7trees = [16, 22, 23, 83, 90]
create_clique(co4G, ves7trees)
add_clique_counts(co4G_cliques, ves7trees)

# VES-09
ves9trees = [16, 22, 23, 24, 25]
create_clique(co4G, ves9trees)
add_clique_counts(co4G_cliques, ves9trees)

# VES-10
ves10trees = [22, 23]
create_clique(co4G, ves10trees)
add_clique_counts(co4G_cliques, ves10trees)

# VES-12
ves12trees = [23]
create_clique(co4G, ves12trees)
add_clique_counts(co4G_cliques, ves12trees)

# VES-13
ves13trees = [23]
create_clique(co4G, ves13trees)
add_clique_counts(co4G_cliques, ves13trees)

# VIN-02
vin2trees = [16]
create_clique(co4G, vin2trees)
add_clique_counts(co4G_cliques, vin2trees)

# VIN-03
vin3trees = [23, 83]
create_clique(co4G, vin3trees)
add_clique_counts(co4G_cliques, vin3trees)

# VIN-05
vin5trees = [57, 85, 90]
create_clique(co4G, vin5trees)
add_clique_counts(co4G_cliques, vin5trees)

# VIN-06
vin6trees = [22, 23]
create_clique(co4G, vin6trees)
add_clique_counts(co4G_cliques, vin6trees)

# VIN-07
vin7trees = [25]
create_clique(co4G, vin7trees)
add_clique_counts(co4G_cliques, vin7trees)

# VIN-08
vin8trees = [22, 23]
create_clique(co4G, vin8trees)
add_clique_counts(co4G_cliques, vin8trees)

print("\nCOHORT 4 GRAPH:")
print("\nVertex clique count:")
print(dict(sorted(co4G_cliques.items(), key=lambda x:x[1], reverse=True)))
co4G_cc = approximation.average_clustering(co4G)
print("Clustering coefficient: ", co4G_cc)
co4G_dc = nx.degree_centrality(co4G)
print("Highest degree centrality: Node %d at %5.4f "%(max(co4G_dc, key=co4G_dc.get), max(co4G_dc.values())))
co4G_ec = nx.eigenvector_centrality(co4G)
print("Highest eigenvector centrality: Node %d at %5.4f "%(max(co4G_ec, key=co4G_ec.get), max(co4G_ec.values())))
co4G_bc = nx.betweenness_centrality(co4G)
print("Highest betweenness centrality: Node %d at %5.4f "%(max(co4G_bc, key=co4G_bc.get), max(co4G_bc.values())))
co4G_mnd = calc_mean_node_degree(co4G)
print("Mean Node Degree: ", co4G_mnd)

nx.draw(co4G, with_labels=True)
plt.show()