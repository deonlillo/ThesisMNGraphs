import networkx as nx
import matplotlib.pyplot as plt
from netgraph import Graph, InteractiveGraph, EditableGraph
from networkx.algorithms import approximation
from random import sample

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

tree_cohorts = {37:1,38:1,39:1,40:1,42:1,43:1,3:2,4:2,7:2,10:2,11:2,13:2,14:2,15:2,26:2,27:2,28:2,29:2,30:2,31:2,32:2,33:2,34:2,35:2,36:2,41:2,44:2,46:2,47:2,50:2,53:2,54:2,55:2,56:2,59:2,60:2,62:2,69:2,76:2,77:2,78:2,79:2,81:2,88:2,1:3,2:3,5:3,6:3,8:3,9:3,12:3,17:3,18:3,19:3,20:3,21:3,45:3,48:3,49:3,51:3,52:3,61:3,74:3,75:3,87:3,89:3,91:3,16:4,22:4,23:4,24:4,25:4,57:4,64:4,83:4,85:4,86:4,90:4}

G = nx.Graph()
G_cliques = {}
#16, 23
# R. vesiculosus genets
# VES-01
ves1trees = [3, 4, 50, 53, 54, 5, 6, 9, 17, 18, 20, 49, 51, 52, 87, 16, 23, 64, 86] # 18-core graph nodes!!!
create_clique(G, ves1trees)
add_clique_counts(G_cliques, ves1trees)

# VES-02
ves2trees = [3, 4, 9, 52, 24, 83, 90]
create_clique(G, ves2trees)
add_clique_counts(G_cliques, ves2trees)

# VES-03
ves3trees = [62, 9, 49, 87, 23, 85]
create_clique(G, ves3trees)
add_clique_counts(G_cliques, ves3trees)

# VES-04
ves4trees = [87]
create_clique(G, ves4trees)
add_clique_counts(G_cliques, ves4trees)

# VES-05
ves5trees = [87]
create_clique(G, ves5trees)
add_clique_counts(G_cliques, ves5trees)

# VES-06
ves6trees = [35, 44, 50, 55, 59, 88, 2, 18, 19, 20, 49, 52, 87, 16, 23, 83, 85, 86]
create_clique(G, ves6trees)
add_clique_counts(G_cliques, ves6trees)

# VES-07
ves7trees = [7, 10, 11, 6, 8, 9, 12, 17, 18, 19, 20, 74, 75, 16, 22, 23, 83, 90]
create_clique(G, ves7trees)
add_clique_counts(G_cliques, ves7trees)

# VES-08
ves8trees = [52]
create_clique(G, ves8trees)
add_clique_counts(G_cliques, ves8trees)

# VES-09
ves9trees = [11, 13, 27, 12, 21, 91, 16, 22, 23, 24, 25]
create_clique(G, ves9trees)
add_clique_counts(G_cliques, ves9trees)

# VES-10
ves10trees = [40, 30, 9, 20, 21, 22, 23]
create_clique(G, ves10trees)
add_clique_counts(G_cliques, ves10trees)

# VES-11
ves11trees = [79]
create_clique(G, ves11trees)
add_clique_counts(G_cliques, ves11trees)

# VES-12
ves12trees = [9, 23]
create_clique(G, ves12trees)
add_clique_counts(G_cliques, ves12trees)

# VES-13
ves13trees = [11, 81, 9, 23]
create_clique(G, ves13trees)
add_clique_counts(G_cliques, ves13trees)

# R. vinicolor genets
# VIN-01
vin1trees = [69, 6, 9, 12]
create_clique(G, vin1trees)
add_clique_counts(G_cliques, vin1trees)

# VIN-02
vin2trees = [14, 15, 9, 16]
create_clique(G, vin2trees)
add_clique_counts(G_cliques, vin2trees)

# VIN-03
vin3trees = [40, 41, 23, 83]
create_clique(G, vin3trees)
add_clique_counts(G_cliques, vin3trees)

# VIN-04
vin4trees = [27, 31, 12]
create_clique(G, vin4trees)
add_clique_counts(G_cliques, vin4trees)

# VIN-05
vin5trees = [50, 54, 55, 56, 49, 87, 89, 57, 85, 90]
create_clique(G, vin5trees)
add_clique_counts(G_cliques, vin5trees)

# VIN-06
vin6trees = [30, 22, 23]
create_clique(G, vin6trees)
add_clique_counts(G_cliques, vin6trees)

# VIN-07
vin7trees = [25]
create_clique(G, vin7trees)
add_clique_counts(G_cliques, vin7trees)

# VIN-08
vin8trees = [18, 21, 22, 23]
create_clique(G, vin8trees)
add_clique_counts(G_cliques, vin8trees)

# VIN-09
vin9trees = [3, 4, 87]
create_clique(G, vin9trees)
add_clique_counts(G_cliques, vin9trees)

# VIN-10
vin10trees = [7]
create_clique(G, vin10trees)
add_clique_counts(G_cliques, vin10trees)

# VIN-11
vin11trees = [17]
create_clique(G, vin11trees)
add_clique_counts(G_cliques, vin11trees)

# VIN-12
vin12trees = [3, 4, 5, 6, 9]
create_clique(G, vin12trees)
add_clique_counts(G_cliques, vin12trees)

#non-linked trees (no fungi found on roots)
em_trees = len(G.nodes)
non_fungi_trees = [37, 38, 39, 42, 43, 26, 28, 29, 32, 33, 34, 36, 46, 47, 60, 76, 77, 78, 1, 45, 48, 61]
for tree in non_fungi_trees:
   G.add_node(tree)

iso_verts = []
for g_node in G.nodes:
   if G.degree(g_node) == 0:
      iso_verts.append(g_node)
      
for vert in iso_verts:
   G.remove_node(vert)

G_aspt = nx.average_shortest_path_length(G)
for iso_vert in iso_verts:
   G.add_node(iso_vert)

print("GRAPH METRICS:")
print("Total EM Colonized Trees:", em_trees)
print("Total Links:", len(G.edges))
G_mnd = calc_mean_node_degree(G)
print("Mean Node Degree:", G_mnd)
print("Mean Path Length Between Linked Tree Pairs:", G_aspt)
G_cc = nx.average_clustering(G)
print("Clustering coefficient:", G_cc)
G_dc = nx.degree_centrality(G)
print("Highest degree centrality: Node %d at %5.4f "%(max(G_dc, key=G_dc.get), max(G_dc.values())))
G_ec = nx.eigenvector_centrality(G)
print("Highest eigenvector centrality: Node %d at %5.4f "%(max(G_ec, key=G_ec.get), max(G_ec.values())))
G_bc = nx.betweenness_centrality(G)
print("Highest betweenness centrality: Node %d at %5.4f "%(max(G_bc, key=G_bc.get), max(G_bc.values())))

print("\nVertex clique count:")
print(dict(sorted(G_cliques.items(), key=lambda x:x[1], reverse=True)))

node_sizes = []
node_colors = []
for node in G.nodes:
   if tree_cohorts[node] == 1:
      node_sizes.append(100)
      node_colors.append("#98FB98") # pale green
   elif tree_cohorts[node] == 2:
      node_sizes.append(600)
      node_colors.append("#32CD32") # lime green
   elif tree_cohorts[node] == 3:
      node_sizes.append(1100)
      node_colors.append("#228B22") # forest green
   elif tree_cohorts[node] == 4:
      node_sizes.append(1600)
      node_colors.append("#006400") # dark green

nx.draw(G, pos=nx.kamada_kawai_layout(G), node_size=node_sizes, node_color=node_colors, with_labels=True)
plt.show()

# -------------------------------- RANDOM TREE REMOVAL ------------------------------------------

G_k_core = nx.k_core(G)
num_random_nodes_to_remove = len(G_k_core)
#print(num_random_nodes_to_remove)
#print(sample(G.nodes,num_random_nodes_to_remove))
random_nodes_to_remove = sample(G.nodes,num_random_nodes_to_remove)
print("\nNodes removed: ", random_nodes_to_remove)

rand_nodes_G = nx.Graph()
for rand_node in random_nodes_to_remove:
   rand_nodes_G.add_node(rand_node)
   G.remove_node(rand_node)

node_sizes = []
node_colors = []
for node in rand_nodes_G.nodes:
   if tree_cohorts[node] == 1:
      node_sizes.append(100)
      node_colors.append("#98FB98") # pale green
   elif tree_cohorts[node] == 2:
      node_sizes.append(600)
      node_colors.append("#32CD32") # lime green
   elif tree_cohorts[node] == 3:
      node_sizes.append(1100)
      node_colors.append("#228B22") # forest green
   elif tree_cohorts[node] == 4:
      node_sizes.append(1600)
      node_colors.append("#006400") # dark green

nx.draw(rand_nodes_G, pos=nx.kamada_kawai_layout(rand_nodes_G), node_size=node_sizes, node_color=node_colors, with_labels=True)
plt.show()

iso_verts = []
for g_node in G.nodes:
   if G.degree(g_node) == 0:
      iso_verts.append(g_node)
      
for vert in iso_verts:
   G.remove_node(vert)

G_aspt_new = nx.average_shortest_path_length(G)
for iso_vert in iso_verts:
   G.add_node(iso_vert)

print("\nGRAPH METRICS AFTER RANDOM TREE REMOVAL:")

G_mnd = calc_mean_node_degree(G)
print("Mean Node Degree:", G_mnd)
print("Mean Path Length Between Linked Tree Pairs:", G_aspt_new)
G_cc = nx.average_clustering(G)
print("Clustering coefficient:", G_cc)
G_dc = nx.degree_centrality(G)
print("Highest degree centrality: Node %d at %5.4f "%(max(G_dc, key=G_dc.get), max(G_dc.values())))
G_ec = nx.eigenvector_centrality(G)
print("Highest eigenvector centrality: Node %d at %5.4f "%(max(G_ec, key=G_ec.get), max(G_ec.values())))
G_bc = nx.betweenness_centrality(G)
print("Highest betweenness centrality: Node %d at %5.4f "%(max(G_bc, key=G_bc.get), max(G_bc.values())))

node_sizes = []
node_colors = []
for node in G.nodes:
   if tree_cohorts[node] == 1:
      node_sizes.append(100)
      node_colors.append("#98FB98") # pale green
   elif tree_cohorts[node] == 2:
      node_sizes.append(600)
      node_colors.append("#32CD32") # lime green
   elif tree_cohorts[node] == 3:
      node_sizes.append(1100)
      node_colors.append("#228B22") # forest green
   elif tree_cohorts[node] == 4:
      node_sizes.append(1600)
      node_colors.append("#006400") # dark green

nx.draw(G, pos=nx.kamada_kawai_layout(G), node_size=node_sizes, node_color=node_colors, with_labels=True)
plt.show()