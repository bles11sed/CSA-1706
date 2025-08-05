from itertools import permutations

dist = {
    ('A', 'B'): 10, ('A', 'C'): 15, ('A', 'D'): 20,
    ('B', 'C'): 35, ('B', 'D'): 25,
    ('C', 'D'): 30,
}
dist.update({(b, a): v for (a, b), v in dist.items()})

cities = ['A', 'B', 'C', 'D']
shortest = float('inf')
for path in permutations(cities[1:]):
    path = ['A'] + list(path) + ['A']
    cost = sum(dist[(path[i], path[i+1])] for i in range(len(path)-1))
    if cost < shortest:
        shortest = cost
        best = path
print("Best path:", best, "Cost:", shortest)
