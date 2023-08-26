# floyd warshall algorithm for shortest path in weighted edge directional graphs
inf = float("inf")

no_vertices = 4

# graph = [[0, 5, inf, 10],
#          [inf, 0, 3, inf],
#          [inf, inf, 0, 1],
#          [inf, inf, inf, 0]]

graph = [[0,    2,  3,  1,  inf,inf],
         [inf,  0,  inf,inf,7,  inf],
         [inf,  inf,0,  inf,inf,3],
         [inf,  inf,inf,0,  5,  2],
         [inf,  inf,inf,inf,0,  inf],
         [inf,  inf,inf,inf,3,  0]]
print(graph)

dist = list(map(lambda i: list(map(lambda j: j, i)), graph))

for i in range(no_vertices):
    for j in range(no_vertices):
        for k in range(no_vertices):
            dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])

print(dist)
