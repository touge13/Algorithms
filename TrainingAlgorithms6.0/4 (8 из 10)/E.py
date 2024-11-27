import sys
sys.setrecursionlimit(200000)

def calculate_subtree_sizes(v, parent):
    subtree_size[v] = 1
    for neighbor in graph[v]:
        if neighbor != parent:
            calculate_subtree_sizes(neighbor, v)
            subtree_size[v] += subtree_size[neighbor]

n = int(input())
graph = {}
for _ in range(n - 1):
    u, v = map(int, input().split())
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append(v)
    graph[v].append(u)

subtree_size = [0] * (n + 1)
calculate_subtree_sizes(1, -1)
print(' '.join(map(str, subtree_size[1:])))
