import networkx as nx
import matplotlib.pyplot as plt
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

# -------------------------------------------- PLOT 4 RANDOM TREE REMOVAL ---------------------------------------------

plot_4_G_k_core = nx.k_core(plot_4_G)
num_random_nodes_to_remove = len(plot_4_G_k_core)
#print(num_random_nodes_to_remove)
#print(sample(G.nodes,num_random_nodes_to_remove))
random_nodes_to_remove = sample(plot_4_G.nodes,num_random_nodes_to_remove)
print("\nNodes removed: ", random_nodes_to_remove)

rand_nodes_G = nx.Graph()
for rand_node in random_nodes_to_remove:
   rand_nodes_G.add_node(rand_node)
   plot_4_G.remove_node(rand_node)
nx.draw(rand_nodes_G, node_size=1000, pos=nx.kamada_kawai_layout(rand_nodes_G), node_color="#2E8B57", with_labels=True) # sea green
plt.show()

iso_verts = []
for g_node in plot_4_G.nodes:
   if plot_4_G.degree(g_node) == 0:
      iso_verts.append(g_node)
      
for vert in iso_verts:
   plot_4_G.remove_node(vert)

try:
   G_aspt_new = nx.average_shortest_path_length(plot_4_G)
except nx.NetworkXError:
   G_aspt_new = "no aspt"

for iso_vert in iso_verts:
   plot_4_G.add_node(iso_vert)

print("\nGRAPH METRICS AFTER RANDOM TREE REMOVAL:")

G_mnd = calc_mean_node_degree(plot_4_G)
print("Mean Node Degree:", G_mnd)
print("Mean Path Length Between Linked Tree Pairs:", G_aspt_new)
G_cc = nx.average_clustering(plot_4_G)
print("Clustering coefficient:", G_cc)
G_dc = nx.degree_centrality(plot_4_G)
print("Highest degree centrality: Node %d at %5.4f "%(max(G_dc, key=G_dc.get), max(G_dc.values())))
G_ec = nx.eigenvector_centrality(plot_4_G)
print("Highest eigenvector centrality: Node %d at %5.4f "%(max(G_ec, key=G_ec.get), max(G_ec.values())))
G_bc = nx.betweenness_centrality(plot_4_G)
print("Highest betweenness centrality: Node %d at %5.4f "%(max(G_bc, key=G_bc.get), max(G_bc.values())))
print("EDGES: ", plot_4_G.edges)

nx.draw(plot_4_G, node_size=1000, pos=nx.kamada_kawai_layout(plot_4_G), node_color="#2E8B57", with_labels=True) # sea green
plt.show()