from collections import deque

def calculate_tree_value(current_node, visited_nodes, tree):
    result = 1
    queue = deque([(current_node, -1)])
    can_flip = False
    while queue:
        multi_child_count = 0
        current_node, parent_node = queue.popleft()
        visited_nodes.add(current_node)
        for neighbor in tree[current_node]:
            if neighbor != parent_node and neighbor in visited_nodes:
                return None
            if len(tree[neighbor]) > 1:
                if neighbor != parent_node:
                    queue.append((neighbor, current_node))
                multi_child_count += 1
            else:
                visited_nodes.add(neighbor)
        if multi_child_count > 2:
            return None
        if multi_child_count == 0:
            can_flip = True
        result *= factorial_table[len(tree[current_node]) - multi_child_count]
    if not can_flip:
        result *= 2
    return result * 2

N, M, K = map(int, input().split())
edges = []
for _ in range(M):
    edges.append(tuple(map(int, input().split())))

tree = {}
for edge in edges:
    u, v = edge
    if u not in tree:
        tree[u] = []
    if v not in tree:
        tree[v] = []
    tree[u].append(v)
    tree[v].append(u)

factorial_table = [1]
for i in range(1, N + 2):
    factorial_table.append((factorial_table[-1] * i) % K)

visited_nodes = set()
tree_count = 0
final_result = 1

for node in tree:
    if node in visited_nodes:
        continue
    tree_count += 1
    tree_value = calculate_tree_value(node, visited_nodes, tree)
    if tree_value is None:
        print(0)
        break
    final_result = (final_result * tree_value) % K
else:
    free_count = N - len(visited_nodes)
    result = 1
    for i in range(free_count):
        result *= i + len(visited_nodes) + 2
        result = result % K
    final_result = (final_result * factorial_table[tree_count] * result) % K
    print(final_result % K)
