import sys

def build_tree(n):
    parent = {}
    for _ in range(n - 1):
        child, par = input().split()
        parent[child] = par
    return parent

def find_lca(a, b, parent):
    ancestors_a = set()
    while a in parent:
        ancestors_a.add(a)
        a = parent[a]
    ancestors_a.add(a)
    while b not in ancestors_a:
        b = parent[b]    
    return b

def process_queries(N):
    parent = build_tree(N)
    q = sys.stdin.readline().strip().split()
    while q:
        a, b = q
        print(find_lca(a, b, parent))
        q = sys.stdin.readline().strip().split()

N = int(input())
process_queries(N)
