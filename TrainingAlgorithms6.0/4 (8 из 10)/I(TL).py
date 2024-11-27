import sys
sys.setrecursionlimit(200000)

def dfs(graph, maxLength, u, v):
	totalLength = 0
	firstLongest = secondLongest = 0

	for i in range(len(graph[u])):
		if (graph[u][i] == v):
			continue
		totalLength = max(totalLength, dfs(graph, maxLength, graph[u][i], u)) 
		if (maxLength[0] > firstLongest):
			secondLongest = firstLongest 
			firstLongest = maxLength[0]
		else:
			secondLongest = max(secondLongest, maxLength[0])
	maxLength[0] = firstLongest + 1
	totalLength = max(totalLength, firstLongest + secondLongest)
	return totalLength

N = int(input())
graph = [[] for _ in range(N)]

for _ in range(N - 1):
    u, v = map(int, input().split())
    graph[u - 1].append(v - 1)
    graph[v - 1].append(u - 1)

res = float("-inf")
path1Length = path2Length = None
for i in range(N):
    for j in range(len(graph[i])):
        maxLength = [0] 
        path1Length = dfs(graph, maxLength, graph[i][j], i) 
        maxLength = [0] 
        path2Length = dfs(graph, maxLength, i, graph[i][j]) 
        res = max(res, path1Length * path2Length)
print(res)