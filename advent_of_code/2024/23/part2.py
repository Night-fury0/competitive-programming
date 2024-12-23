import networkx as nx
from itertools import combinations

lines = ""
with open("input.txt","r") as f:
    lines = f.read().strip().split("\n")

points = set()
G = nx.Graph()
links = []

for line in lines:
    a,b = line.split("-")
    links.append((a,b))
    points.add(a)
    points.add(b)

G.add_edges_from(links)

cliques = list(nx.find_cliques(G))

largest = max(cliques,key=len)

password = sorted(largest)

print(",".join(password))
