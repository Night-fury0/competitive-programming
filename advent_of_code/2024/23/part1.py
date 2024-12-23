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
print(len(links))

count = 0
for comb in list(combinations(points,3)):
    a,b,c = comb
    if (a.startswith("t") or b.startswith("t") or c.startswith("t")) and ((G.has_edge(a,b) and G.has_edge(b,c) and G.has_edge(a,c))):
        print(comb)
        count += 1

print(count)


    

