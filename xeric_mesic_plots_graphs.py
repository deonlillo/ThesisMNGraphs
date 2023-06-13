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

def calc_mean_node_degree(G):
   total_node_degree = 0
   for node in G.nodes:
      total_node_degree += G.degree(node)
   mean_node_degree = total_node_degree / len(G.nodes)
   return mean_node_degree

# PLOT 1
#plot_1_G = nx.Graph()
#plot_1_G_cliques = {}

# VES-1-01
# Plot 1 (xeric)
#ves1_1trees = [20, 4, 61, 19, 25, 21, 1, 22, 8, 38, 23, 26, 5, 41, 49, 79, 62, 81, 42, 37, 36, "U3", 35]
#create_clique(plot_1_G, ves1_1trees)
#add_clique_counts(plot_1_G_cliques, ves1_1trees)

# VES-1-02
# Plot 1 (xeric)
#ves1_2trees = [48]
#create_clique(plot_1_G, ves1_2trees)
#add_clique_counts(plot_1_G_cliques, ves1_2trees)

# VES-1-03
# Plot 1 (xeric)
#ves1_3trees = [41, 48]
#create_clique(plot_1_G, ves1_3trees)
#add_clique_counts(plot_1_G_cliques, ves1_3trees)

# VES-1-04
# Plot 1 (xeric)
#ves1_4trees = [19]
#create_clique(plot_1_G, ves1_4trees)
#add_clique_counts(plot_1_G_cliques, ves1_4trees)

# VIN-1-01
# Plot 1 (xeric)
#vin1_1trees = [1, 23, 33, 57, 26]
#create_clique(plot_1_G, vin1_1trees)
#add_clique_counts(plot_1_G_cliques, vin1_1trees)

#print("Total linked nodes:", len(plot_1_G))
#print("Total links:", len(plot_1_G.edges))
#print(plot_1_G.edges)

# ISOLATES
# VIN-1-02
# Plot 1 (xeric)
# vin1_2trees = [80] # ISOLATED VERTEX
# create_clique(plot_1_G, vin1_2trees)
# add_clique_counts(plot_1_G_cliques, vin1_2trees)

# Plot 1 (xeric)
#plot1_isolates = [80, -1, -2]
#for tree in plot1_isolates:
#   plot_1_G.add_node(tree)

#print("PLOT 1:")
#plot_1_G_mnd = calc_mean_node_degree(plot_1_G)
##print("Mean Node Degree:", plot_1_G_mnd)
#plot_1_G_cc = nx.average_clustering(plot_1_G)
#print("Clustering coefficient:", plot_1_G_cc)

#nx.draw(plot_1_G, with_labels=True)
#plt.show()

# PLOT 2
#plot_2_G = nx.Graph()
#plot_2_G_cliques = {}

# VES-2-01
# Plot 2 (xeric)
#ves2_1trees = [11, 9, 10, 58, 6, 8, 7, 12, 4, 48]
#create_clique(plot_2_G, ves2_1trees)
#add_clique_counts(plot_2_G_cliques, ves2_1trees)

# VES-2-02
# Plot 2 (xeric)
#ves2_2trees = [9]
#create_clique(plot_2_G, ves2_2trees)
#add_clique_counts(plot_2_G_cliques, ves2_2trees)

# VIN-2-01
# Plot 2 (xeric)
#vin2_1trees = [6]
#create_clique(plot_2_G, vin2_1trees)
#add_clique_counts(plot_2_G_cliques, vin2_1trees)

# VIN-2-02
# Plot 2 (xeric)
#vin2_2trees = [11, 12, 10]
#create_clique(plot_2_G, vin2_2trees)
#add_clique_counts(plot_2_G_cliques, vin2_2trees)

# VIN-2-03
# Plot 2 (xeric)
#vin2_3trees = [6, 58, 9, 10, 7, 11, 13, "U1", 61, 4]
#create_clique(plot_2_G, vin2_3trees)
#add_clique_counts(plot_2_G_cliques, vin2_3trees)

# VIN-2-04
# Plot 2 (xeric)
#vin2_4trees = [6]
#create_clique(plot_2_G, vin2_4trees)
#add_clique_counts(plot_2_G_cliques, vin2_4trees)

#print("\nPLOT 2:")
#plot_2_G_mnd = calc_mean_node_degree(plot_2_G)
#print("Mean Node Degree:", plot_2_G_mnd)
#plot_2_G_cc = nx.average_clustering(plot_2_G)
#print("Clustering coefficient:", plot_2_G_cc)

#print(len(plot_2_G))
#print(len(plot_2_G.edges))
#nx.draw(plot_2_G, with_labels=True)
#plt.show()

# PLOT 3
plot_3_G = nx.Graph()
plot_3_G_cliques = {}

# VES-3-01
# Plot 3 (xeric)
ves3_1trees = [2, 1, 17, 3, 48, 14, 19, 13, 74, 52, 41, 25, 26, 16, 49, 20, 15, 32, 111, 113, 44, 46]
create_clique(plot_3_G, ves3_1trees)
add_clique_counts(plot_3_G_cliques, ves3_1trees)

# VES-3-02
# Plot 3 (xeric)
ves3_2trees = [1]
create_clique(plot_3_G, ves3_2trees)
add_clique_counts(plot_3_G_cliques, ves3_2trees)

# VES-3-03
# Plot 3 (xeric)
ves3_3trees = [2, 115]
create_clique(plot_3_G, ves3_3trees)
add_clique_counts(plot_3_G_cliques, ves3_3trees)

# VES-3-04
# Plot 3 (xeric)
ves3_4trees = [19, 109, 82, 47]
create_clique(plot_3_G, ves3_4trees)
add_clique_counts(plot_3_G_cliques, ves3_4trees)

# VIN-3-01
# Plot 3 (xeric)
vin3_1trees = [3, 18, 1, 48, 19, 113, 51]
create_clique(plot_3_G, vin3_1trees)
add_clique_counts(plot_3_G_cliques, vin3_1trees)

# VIN-3-02
# Plot 3 (xeric)
vin3_2trees = [17, 18]
create_clique(plot_3_G, vin3_2trees)
add_clique_counts(plot_3_G_cliques, vin3_2trees)

# VIN-3-03
# Plot 3 (xeric)
vin3_3trees = [17]
create_clique(plot_3_G, vin3_3trees)
add_clique_counts(plot_3_G_cliques, vin3_3trees)

# VIN-3-04
# Plot 3 (xeric)
vin3_4trees = [19, 2, 1, 14, 15, 113, 19, 13, 17, 118, 31, 41, 21, 25]
create_clique(plot_3_G, vin3_4trees)
add_clique_counts(plot_3_G_cliques, vin3_4trees)

# VIN-3-05
# Plot 3 (xeric)
vin3_5trees = [1]
create_clique(plot_3_G, vin3_5trees)
add_clique_counts(plot_3_G_cliques, vin3_5trees)

plot_3_G_aspt = nx.average_shortest_path_length(plot_3_G)

print("\nPLOT 3:")
print("Total linked nodes:", len(plot_3_G))
print("Total links:", len(plot_3_G.edges))

# ISOLATES
# Plot 3 (xeric)
plot3_isolates = [-1, -2]
for tree in plot3_isolates:
   plot_3_G.add_node(tree)

plot_3_G_mnd = calc_mean_node_degree(plot_3_G)
print("Mean Node Degree:", plot_3_G_mnd)
plot_3_G_cc = nx.average_clustering(plot_3_G)
print("Clustering coefficient:", plot_3_G_cc)
print("Mean Path Length Between Linked Tree Pairs:", plot_3_G_aspt)
plot_3_G_dc = nx.degree_centrality(plot_3_G)
print("Highest degree centrality: Node %d at %5.4f "%(max(plot_3_G_dc, key=plot_3_G_dc.get), max(plot_3_G_dc.values())))
plot_3_G_ec = nx.eigenvector_centrality(plot_3_G)
print("Highest eigenvector centrality: Node %d at %5.4f "%(max(plot_3_G_ec, key=plot_3_G_ec.get), max(plot_3_G_ec.values())))
plot_3_G_bc = nx.betweenness_centrality(plot_3_G)
print("Highest betweenness centrality: Node %d at %5.4f "%(max(plot_3_G_bc, key=plot_3_G_bc.get), max(plot_3_G_bc.values())))

nx.draw(plot_3_G, node_size=1000, pos=nx.kamada_kawai_layout(plot_3_G), node_color="#ADFF2F", with_labels=True) # green yellow
plt.show()

# ---------------------------------------- PLOT 3 K-CORE -------------------------------------------------------

plot_3_G_k_core = nx.k_core(plot_3_G) # core number: 21
print(nx.core_number(plot_3_G_k_core))

nx.draw(plot_3_G_k_core, node_size=1000, pos=nx.kamada_kawai_layout(plot_3_G_k_core), node_color="#ADFF2F", with_labels=True)
plt.show()

for n in plot_3_G_k_core.nodes:
   plot_3_G.remove_node(n)

print("\nNEW METRICS AFTER K-CORE PARTITIONING:")
plot_3_G_mnd = calc_mean_node_degree(plot_3_G)
print("Mean Node Degree:", plot_3_G_mnd)
plot_3_G_cc = nx.average_clustering(plot_3_G)
print("Clustering coefficient:", plot_3_G_cc)
plot_3_G_dc = nx.degree_centrality(plot_3_G)
print("Highest degree centrality: Node %d at %5.4f "%(max(plot_3_G_dc, key=plot_3_G_dc.get), max(plot_3_G_dc.values())))
plot_3_G_ec = nx.eigenvector_centrality(plot_3_G)
print("Highest eigenvector centrality: Node %d at %5.4f "%(max(plot_3_G_ec, key=plot_3_G_ec.get), max(plot_3_G_ec.values())))
plot_3_G_bc = nx.betweenness_centrality(plot_3_G)
print("Highest betweenness centrality: Node %d at %5.4f "%(max(plot_3_G_bc, key=plot_3_G_bc.get), max(plot_3_G_bc.values())))

nx.draw(plot_3_G, pos=nx.kamada_kawai_layout(plot_3_G), node_size=1000, node_color="#ADFF2F", with_labels=True)
plt.show()

#for vert in iso_verts:
#   G.remove_node(vert)

#G.remove_node(14)
#G.remove_node(15) # linked to each other separate from main connectivity network

#G_aspt = nx.average_shortest_path_length(G)
#print("Mean Path Length Between Linked Tree Pairs:", G_aspt)
















# PLOT 4
plot_4_G = nx.Graph()
plot_4_G_cliques = {}

# VES-4-01
# Plot 4 (mesic)
ves4_1trees = [12, 19, 17, 40]
create_clique(plot_4_G, ves4_1trees)
add_clique_counts(plot_4_G_cliques, ves4_1trees)

# VES-4-02
# Plot 4 (mesic)
ves4_2trees = [12, 56, 54, 47, 52, 1, 2, 92, 14, 3, 73, 16, 100, 21, 11, 37, 17, 19, 66]
create_clique(plot_4_G, ves4_2trees)
add_clique_counts(plot_4_G_cliques, ves4_2trees)

# VES-4-03
# Plot 4 (mesic)
ves4_3trees = [1, 7, 3, 6]
create_clique(plot_4_G, ves4_3trees)
add_clique_counts(plot_4_G_cliques, ves4_3trees)

# VES-4-04
# Plot 4 (mesic)
ves4_4trees = [100, 7]
create_clique(plot_4_G, ves4_4trees)
add_clique_counts(plot_4_G_cliques, ves4_4trees)

# VIN-4-01
# Plot 4 (mesic)
vin4_1trees = [59, 1, 3, 11]
create_clique(plot_4_G, vin4_1trees)
add_clique_counts(plot_4_G_cliques, vin4_1trees)

# VIN-4-02
# Plot 4 (mesic)
vin4_2trees = [39, 76, 54, 7, 1, 12, 11, 14, 2, 3, 16, 17, 40, 20, 56, 15]
create_clique(plot_4_G, vin4_2trees)
add_clique_counts(plot_4_G_cliques, vin4_2trees)

plot_4_G_aspt = nx.average_shortest_path_length(plot_4_G)

print("\nPLOT 4:")

print("Total linked nodes:", len(plot_4_G))
print("Total links", len(plot_4_G.edges))

# ISOLATES
# Plot 4 (mesic)
plot4_isolates = [-1, -2]
for tree in plot4_isolates:
   plot_4_G.add_node(tree)

plot_4_G_mnd = calc_mean_node_degree(plot_4_G)
print("Mean Node Degree:", plot_4_G_mnd)
plot_4_G_cc = nx.average_clustering(plot_4_G)
print("Clustering coefficient:", plot_4_G_cc)
print("Mean Path Length Between Linked Tree Pairs:", plot_4_G_aspt)
plot_4_G_dc = nx.degree_centrality(plot_4_G)
print("Highest degree centrality: Node %d at %5.4f "%(max(plot_4_G_dc, key=plot_4_G_dc.get), max(plot_4_G_dc.values())))
plot_4_G_ec = nx.eigenvector_centrality(plot_4_G)
print("Highest eigenvector centrality: Node %d at %5.4f "%(max(plot_4_G_ec, key=plot_4_G_ec.get), max(plot_4_G_ec.values())))
plot_4_G_bc = nx.betweenness_centrality(plot_4_G)
print("Highest betweenness centrality: Node %d at %5.4f "%(max(plot_4_G_bc, key=plot_4_G_bc.get), max(plot_4_G_bc.values())))

nx.draw(plot_4_G, node_size=1000, pos=nx.kamada_kawai_layout(plot_4_G), node_color="#2E8B57", with_labels=True) # sea green
plt.show()


# ---------------------------------------- PLOT 4 K-CORE -------------------------------------------------------

plot_4_G_k_core = nx.k_core(plot_4_G) # core number: 18
print(nx.core_number(plot_4_G_k_core))

nx.draw(plot_4_G_k_core, node_size=1000, pos=nx.kamada_kawai_layout(plot_4_G_k_core), node_color="#2E8B57", with_labels=True)
plt.show()

for n in plot_4_G_k_core.nodes:
   plot_4_G.remove_node(n)

iso_verts = []
for g_node in plot_4_G.nodes:
   if plot_4_G.degree(g_node) == 0:
      iso_verts.append(g_node)

for vert in iso_verts:
   plot_4_G.remove_node(vert)

plot_4_G_aspt = nx.average_shortest_path_length(plot_4_G)
for iso_vert in iso_verts:
   plot_4_G.add_node(iso_vert)

print("\nNEW METRICS AFTER K-CORE PARTITIONING:")
plot_4_G_mnd = calc_mean_node_degree(plot_4_G)
print("Mean Node Degree:", plot_4_G_mnd)
plot_4_G_cc = nx.average_clustering(plot_4_G)
print("Clustering coefficient:", plot_4_G_cc)
print("Mean Path Length Between Linked Tree Pairs:", plot_4_G_aspt)
plot_4_G_dc = nx.degree_centrality(plot_4_G)
print("Highest degree centrality: Node %d at %5.4f "%(max(plot_4_G_dc, key=plot_4_G_dc.get), max(plot_4_G_dc.values())))
plot_4_G_ec = nx.eigenvector_centrality(plot_4_G)
print("Highest eigenvector centrality: Node %d at %5.4f "%(max(plot_4_G_ec, key=plot_4_G_ec.get), max(plot_4_G_ec.values())))
plot_4_G_bc = nx.betweenness_centrality(plot_4_G)
print("Highest betweenness centrality: Node %d at %5.4f "%(max(plot_4_G_bc, key=plot_4_G_bc.get), max(plot_4_G_bc.values())))

nx.draw(plot_4_G, pos=nx.kamada_kawai_layout(plot_4_G), node_size=1000, node_color="#2E8B57", with_labels=True)
plt.show()

#for vert in iso_verts:
#   G.remove_node(vert)

#G.remove_node(14)
#G.remove_node(15) # linked to each other separate from main connectivity network

#G_aspt = nx.average_shortest_path_length(G)
#print("Mean Path Length Between Linked Tree Pairs:", G_aspt)













# PLOT 5
#plot_5_G = nx.Graph()
#plot_5_G_cliques = {}

# VES-5-01
# Plot 5 (mesic)
#ves5_1trees = [5, 6, 25, 19, 21, 17, 60, 59, 18, 3, 24, "105B", 100, 10, 4]
#create_clique(plot_5_G, ves5_1trees)
#add_clique_counts(plot_5_G_cliques, ves5_1trees)

# VES-5-02
# Plot 5 (mesic)
#ves5_2trees = [10, 57, 4]
#create_clique(plot_5_G, ves5_2trees)
#add_clique_counts(plot_5_G_cliques, ves5_2trees)

# VES-5-03
# Plot 5 (mesic)
#ves5_3trees = ["105A", 24, 10]
#create_clique(plot_5_G, ves5_3trees)
#add_clique_counts(plot_5_G_cliques, ves5_3trees)

# VES-5-04
# Plot 5 (mesic)
#ves5_4trees = [107]
#create_clique(plot_5_G, ves5_4trees)
#add_clique_counts(plot_5_G_cliques, ves5_4trees)

# VES-5-05
# Plot 5 (mesic)
#ves5_5trees = [107]
#create_clique(plot_5_G, ves5_5trees)
#add_clique_counts(plot_5_G_cliques, ves5_5trees)

# VES-5-06
# Plot 5 (mesic)
#ves5_6trees = [61, 19, 108, 24, 107, 20, 100, 21, "105B", 17]
#create_clique(plot_5_G, ves5_6trees)
#add_clique_counts(plot_5_G_cliques, ves5_6trees)

# VES-5-07
# Plot 5 (mesic)
#ves5_7trees = [12, 7, 130, 20, 18, 19, 17, 100, 24, 21, 86]
#create_clique(plot_5_G, ves5_7trees)
#add_clique_counts(plot_5_G_cliques, ves5_7trees)

# VIN-5-01
# Plot 5 (mesic)
#vin5_1trees = [16, 15, 17]
#create_clique(plot_5_G, vin5_1trees)
#add_clique_counts(plot_5_G_cliques, vin5_1trees)

# VIN-5-02
# Plot 5 (mesic)
#vin5_2trees = [19, 24]
#create_clique(plot_5_G, vin5_2trees)
#add_clique_counts(plot_5_G_cliques, vin5_2trees)

# VIN-5-03
# Plot 5 (mesic)
#vin5_3trees = [18]
#create_clique(plot_5_G, vin5_3trees)
#add_clique_counts(plot_5_G_cliques, vin5_3trees)

# VIN-5-04
# Plot 5 (mesic)
#vin5_4trees = [5, 6, 4]
#create_clique(plot_5_G, vin5_4trees)
#add_clique_counts(plot_5_G_cliques, vin5_4trees)

#print("\nPLOT 5:")
#print("Total linked nodes:", len(plot_5_G))
#print("Total links", len(plot_5_G.edges))

# ISOLATES
# Plot 5 (mesic)
#plot5_isolates = [-1, -2]
#for tree in plot5_isolates:
#   plot_5_G.add_node(tree)

#plot_5_G_mnd = calc_mean_node_degree(plot_5_G)
#print("Mean Node Degree:", plot_5_G_mnd)
#plot_5_G_cc = nx.average_clustering(plot_5_G)
#print("Clustering coefficient:", plot_5_G_cc)

# PLOT 6
#plot_6_G = nx.Graph()
#plot_6_G_cliques = {}

# VES-6-01
# Plot 6 (mesic)
#ves6_1trees = [33, 77, 79, 41, 81, 52, "U8", 59, 53, 35, 44, 1, 8, 10, 9, 37, 14, 7, 23, 117, 40, 45]
#create_clique(plot_6_G, ves6_1trees)
#add_clique_counts(plot_6_G_cliques, ves6_1trees)

# VES-6-02
# Plot 6 (mesic)
#ves6_2trees = [106, 1, 19, 2, 108, 7]
#create_clique(plot_6_G, ves6_2trees)
#add_clique_counts(plot_6_G_cliques, ves6_2trees)

# VES-6-03
# Plot 6 (mesic)
#ves6_3trees = [101, 2, 9, 37, 19]
#create_clique(plot_6_G, ves6_3trees)
#add_clique_counts(plot_6_G_cliques, ves6_3trees)

# VES-6-04
# Plot 6 (mesic)
#ves6_4trees = [1, 36, 10, 2, 7, 19, 5, 121, 33, 117, 17, 11, 56, 45]
#create_clique(plot_6_G, ves6_4trees)
#add_clique_counts(plot_6_G_cliques, ves6_4trees)

# VES-6-05
# Plot 6 (mesic)
#ves6_5trees = [19, 2]
#create_clique(plot_6_G, ves6_5trees)
#add_clique_counts(plot_6_G_cliques, ves6_5trees)

# VES-6-06
# Plot 6 (mesic)
#ves6_6trees = [45]
#create_clique(plot_6_G, ves6_6trees)
#add_clique_counts(plot_6_G_cliques, ves6_6trees)

# VES-6-07
# Plot 6 (mesic)
#ves6_7trees = [23]
#create_clique(plot_6_G, ves6_7trees)
#add_clique_counts(plot_6_G_cliques, ves6_7trees)

# VIN-6-01
# Plot 6 (mesic)
#vin6_1trees = [1, 3, 7, 8, 10, 37, 14, 61, 12, 117, 60, 35, 36, 38, 56, 2, 44, 41]
#create_clique(plot_6_G, vin6_1trees)
#add_clique_counts(plot_6_G_cliques, vin6_1trees)

# VIN-6-02
# Plot 6 (mesic)
#vin6_2trees = [41, 33, 35, 122, 38, 44]
#create_clique(plot_6_G, vin6_2trees)
#add_clique_counts(plot_6_G_cliques, vin6_2trees)

# VIN-6-03
# Plot 6 (mesic)
#vin6_3trees = [121, 1, 3, 2, 7, 19, 101]
#create_clique(plot_6_G, vin6_3trees)
#add_clique_counts(plot_6_G_cliques, vin6_3trees)

# VIN-6-04
# Plot 6 (mesic)
#vin6_4trees = [35, 36]
#create_clique(plot_6_G, vin6_4trees)
#add_clique_counts(plot_6_G_cliques, vin6_4trees)

# VIN-6-05
# Plot 6 (mesic)
#vin6_5trees = [19]
#create_clique(plot_6_G, vin6_5trees)
#add_clique_counts(plot_6_G_cliques, vin6_5trees)

# VIN-6-06
# Plot 6 (mesic)
#vin6_6trees = [83, 41, 35, 38, 79]
#create_clique(plot_6_G, vin6_6trees)
#add_clique_counts(plot_6_G_cliques, vin6_6trees)

# VIN-6-07
# Plot 6 (mesic)
#vin6_7trees = [35]
#create_clique(plot_6_G, vin6_7trees)
#add_clique_counts(plot_6_G_cliques, vin6_7trees)

# VIN-6-08
# Plot 6 (mesic)
#vin6_8trees = [41]
#create_clique(plot_6_G, vin6_8trees)
#add_clique_counts(plot_6_G_cliques, vin6_8trees)

# VIN-6-09
# Plot 6 (mesic)
#vin6_9trees = [51, 37]
#create_clique(plot_6_G, vin6_9trees)
#add_clique_counts(plot_6_G_cliques, vin6_9trees)

# VIN-6-10
# Plot 6 (mesic)
#vin6_10trees = [9]
#create_clique(plot_6_G, vin6_10trees)
#add_clique_counts(plot_6_G_cliques, vin6_10trees)

#print("\nPLOT 6:")
#print("Total linked nodes:", len(plot_6_G))
#print("Total links:", len(plot_6_G.edges))

# ISOLATES
# Plot 6 (mesic)
#plot6_isolates = [-1, -2]
#for tree in plot6_isolates:
#   plot_6_G.add_node(tree)

#plot_6_G_mnd = calc_mean_node_degree(plot_6_G)
#print("Mean Node Degree:", plot_6_G_mnd)
#plot_6_G_cc = nx.average_clustering(plot_6_G)
#print("Clustering coefficient:", plot_6_G_cc)


example_xeric_G = nx.Graph()
create_clique(example_xeric_G, ves3_4trees)
nx.draw(example_xeric_G, node_size=1000, pos=nx.kamada_kawai_layout(example_xeric_G), node_color="#ADFF2F", with_labels=True) # green yellow
plt.show()

example_mesic_G = nx.Graph()
create_clique(example_mesic_G, ves4_1trees)
nx.draw(example_mesic_G, node_size=1000, pos=nx.kamada_kawai_layout(example_mesic_G), node_color="#2E8B57", with_labels=True) # sea green
plt.show()