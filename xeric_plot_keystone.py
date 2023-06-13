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

# --------------------------------------- PLOT 3 KEYSTONE INDIVIDUAL REMOVAL ---------------------------------------------

plot_3_G.remove_node(19) #keystone individual

iso_verts = []
for g_node in plot_3_G.nodes:
   if plot_3_G.degree(g_node) == 0:
      iso_verts.append(g_node)

for vert in iso_verts:
   plot_3_G.remove_node(vert)
separate_linkage = [109, 47, 82] # linked separately from main connectivity network
for node in separate_linkage:
   plot_3_G.remove_node(node)

plot_3_G_aspt = nx.average_shortest_path_length(plot_3_G)
for iso_vert in iso_verts:
   plot_3_G.add_node(iso_vert)
create_clique(plot_3_G, separate_linkage)

print("\nPLOT 3 AFTER KEYSTONE INDIVIDUAL REMOVAL:")
print("Total linked nodes:", len(plot_3_G.nodes) - len(iso_verts))
print("Total links:", len(plot_3_G.edges))
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