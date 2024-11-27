from collections import deque

def read_input():
    N = int(input())
    if N == 1:
        cost = int(input())
        return N, [], [cost]
    graph = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    costs = list(map(int, input().split()))
    return N, graph, costs

def bfs(graph, start):
    order = []
    queue = deque([start])
    parent = {start: None}
    while queue:
        v = queue.popleft()
        order.append(v)
        for u in graph[v]:
            if u not in parent:
                queue.append(u)
                parent[u] = v
    return order, parent

def iterative_dp(graph, costs, dp):
    order, parent = bfs(graph, 1)
    for v in reversed(order):
        dp[v][0] = 0
        dp[v][1] = costs[v - 1]
        for u in graph[v]:
            if u == parent[v]:
                continue
            dp[v][0] += dp[u][1]
            dp[v][1] += min(dp[u][0], dp[u][1])

def mark(v, parent, must_mark, graph, dp, marked):
    stack = [(v, parent, must_mark)]
    while stack:
        v, p, must_mark = stack.pop()
        if must_mark or dp[v][0] > dp[v][1]:
            marked[v] = True
            must_mark_children = False
        else:
            must_mark_children = True
        for u in graph[v]:
            if u != p:
                stack.append((u, v, must_mark_children))

N, graph, costs = read_input()
if N == 1:
    print(costs[0], 1)
    print(1)
else:
    dp = [[float('inf')] * 2 for _ in range(N + 1)]
    marked = [False] * (N + 1)
    iterative_dp(graph, costs, dp)
    min_cost = min(dp[1][0], dp[1][1])
    if min_cost == dp[1][1]:
        mark(1, -1, True, graph, dp, marked)
    else:
        mark(1, -1, False, graph, dp, marked)
    marked_vertices = [i for i in range(1, N + 1) if marked[i]]
    print(min_cost, len(marked_vertices))
    print(" ".join(map(str, marked_vertices)))
