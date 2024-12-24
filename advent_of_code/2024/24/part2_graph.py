from graphviz import Graph

lines = ""
with open("input.txt","r") as f:
    lines = f.read().strip().split("\n\n")

source = dict()
initial = lines[0].split("\n")
for i in initial:
    k,v = i.split(": ")
    source[k] = int(v)


gates = lines[1].split("\n")

#values = ['z32','z33','z34','z35','z36','z37','z38','z39']

gates = [k.split(" ") for k in gates]

edges = []
for g in gates:  
    edges.append((g[0],g[-1],g[1]))
    edges.append((g[2],g[-1],g[1]))

dot = Graph(comment='problem')
for e in edges:
    dot.edge(e[0],e[1], e[2])

dot.render("problem",format='png',view=True)
