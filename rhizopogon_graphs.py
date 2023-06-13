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

vesG = nx.Graph()
vesG_cliques = {}
vinG = nx.Graph()
vinG_cliques = {}

# R. vesiculosus genets
# VES-01
ves1trees = [3, 4, 50, 53, 54, 5, 6, 9, 17, 18, 20, 49, 51, 52, 87, 16, 23, 64, 86]
create_clique(vesG, ves1trees)
add_clique_counts(vesG_cliques, ves1trees)

# VES-02
ves2trees = [3, 4, 9, 52, 24, 83, 90]
create_clique(vesG, ves2trees)
add_clique_counts(vesG_cliques, ves2trees)

# VES-03
ves3trees = [62, 9, 49, 87, 23, 85]
create_clique(vesG, ves3trees)
add_clique_counts(vesG_cliques, ves3trees)

# VES-04
ves4trees = [87]
create_clique(vesG, ves4trees)
add_clique_counts(vesG_cliques, ves4trees)

# VES-05
ves5trees = [87]
create_clique(vesG, ves5trees)
add_clique_counts(vesG_cliques, ves5trees)

# VES-06
ves6trees = [35, 44, 50, 55, 59, 88, 2, 18, 19, 20, 49, 52, 87, 16, 23, 83, 85, 86]
create_clique(vesG, ves6trees)
add_clique_counts(vesG_cliques, ves6trees)

# VES-07
ves7trees = [7, 10, 11, 6, 8, 9, 12, 17, 18, 19, 20, 74, 75, 16, 22, 23, 83, 90]
create_clique(vesG, ves7trees)
add_clique_counts(vesG_cliques, ves7trees)

# VES-08
ves8trees = [52]
create_clique(vesG, ves8trees)
add_clique_counts(vesG_cliques, ves8trees)

# VES-09
ves9trees = [11, 13, 27, 12, 21, 91, 16, 22, 23, 24, 25]
create_clique(vesG, ves9trees)
add_clique_counts(vesG_cliques, ves9trees)

# VES-10
ves10trees = [40, 30, 9, 20, 21, 22, 23]
create_clique(vesG, ves10trees)
add_clique_counts(vesG_cliques, ves10trees)

# VES-11
ves11trees = [79]
create_clique(vesG, ves11trees)
add_clique_counts(vesG_cliques, ves11trees)

# VES-12
ves12trees = [9, 23]
create_clique(vesG, ves12trees)
add_clique_counts(vesG_cliques, ves12trees)

# VES-13
ves13trees = [11, 81, 9, 23]
create_clique(vesG, ves13trees)
add_clique_counts(vesG_cliques, ves13trees)

# R. vinicolor genets
# VIN-01
vin1trees = [69, 6, 9, 12]
create_clique(vinG, vin1trees)
add_clique_counts(vinG_cliques, vin1trees)

# VIN-02
vin2trees = [14, 15, 9, 16]
create_clique(vinG, vin2trees)
add_clique_counts(vinG_cliques, vin2trees)

# VIN-03
vin3trees = [40, 41, 23, 83]
create_clique(vinG, vin3trees)
add_clique_counts(vinG_cliques, vin3trees)

# VIN-04
vin4trees = [27, 31, 12]
create_clique(vinG, vin4trees)
add_clique_counts(vinG_cliques, vin4trees)

# VIN-05
vin5trees = [50, 54, 55, 56, 49, 87, 89, 57, 85, 90]
create_clique(vinG, vin5trees)
add_clique_counts(vinG_cliques, vin5trees)

# VIN-06
vin6trees = [30, 22, 23]
create_clique(vinG, vin6trees)
add_clique_counts(vinG_cliques, vin6trees)

# VIN-07
vin7trees = [25]
create_clique(vinG, vin7trees)
add_clique_counts(vinG_cliques, vin7trees)

# VIN-08
vin8trees = [18, 21, 22, 23]
create_clique(vinG, vin8trees)
add_clique_counts(vinG_cliques, vin8trees)

# VIN-09
vin9trees = [3, 4, 87]
create_clique(vinG, vin9trees)
add_clique_counts(vinG_cliques, vin9trees)

# VIN-10
vin10trees = [7]
create_clique(vinG, vin10trees)
add_clique_counts(vinG_cliques, vin10trees)

# VIN-11
vin11trees = [17]
create_clique(vinG, vin11trees)
add_clique_counts(vinG_cliques, vin11trees)

# VIN-12
vin12trees = [3, 4, 5, 6, 9]
create_clique(vinG, vin12trees)
add_clique_counts(vinG_cliques, vin12trees)

#print(list(G.nodes))
#print(list(G.edges))
print("\nR. VESICULOSUS GENETS GRAPH:")
print("\nVertex clique count:")
print(dict(sorted(vesG_cliques.items(), key=lambda x:x[1], reverse=True)))
vesG_cc = approximation.average_clustering(vesG)
print("Clustering coefficient: ", vesG_cc)
vesG_dc = nx.degree_centrality(vesG)
print("Highest degree centrality: Node %d at %5.4f "%(max(vesG_dc, key=vesG_dc.get), max(vesG_dc.values())))
vesG_ec = nx.eigenvector_centrality(vesG)
print("Highest eigenvector centrality: Node %d at %5.4f "%(max(vesG_ec, key=vesG_ec.get), max(vesG_ec.values())))
vesG_bc = nx.betweenness_centrality(vesG)
print("Highest betweenness centrality: Node %d at %5.4f "%(max(vesG_bc, key=vesG_bc.get), max(vesG_bc.values())))


nx.draw(vesG, with_labels=True)
plt.show()


print("\nR. VINICOLOR GENETS GRAPH:")
print("\nVertex clique count:")
print(dict(sorted(vinG_cliques.items(), key=lambda x:x[1], reverse=True)))
vinG_cc = approximation.average_clustering(vinG)
print("Clustering coefficient: ", vinG_cc)
vinG_dc = nx.degree_centrality(vinG)
print("Highest degree centrality: Node %d at %5.4f "%(max(vinG_dc, key=vinG_dc.get), max(vinG_dc.values())))
vinG_ec = nx.eigenvector_centrality(vinG)
print("Highest eigenvector centrality: Node %d at %5.4f "%(max(vinG_ec, key=vinG_ec.get), max(vinG_ec.values())))
vinG_bc = nx.betweenness_centrality(vinG)
print("Highest betweenness centrality: Node %d at %5.4f "%(max(vinG_bc, key=vinG_bc.get), max(vinG_bc.values())))




nx.draw(vinG, with_labels=True)
plt.show()



