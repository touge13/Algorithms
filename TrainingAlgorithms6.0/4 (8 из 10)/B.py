import sys

sys.setrecursionlimit(100000)

def count_descendants(person, tree, memo):
    if person in memo:
        return memo[person]
    total_descendants = 0
    for child in tree.get(person, []):
        total_descendants += 1 + count_descendants(child, tree, memo)
    memo[person] = total_descendants
    return total_descendants

N = int(input())
tree = {}
all_people = set()
for _ in range(N - 1):
    child, parent = input().split()
    if parent not in tree:
        tree[parent] = []
    tree[parent].append(child)
    all_people.add(child)
    all_people.add(parent)

memo = {}
for person in tree.keys():
    count_descendants(person, tree, memo)
for person in all_people:
    if person not in memo:
        memo[person] = 0

for person in sorted(memo.keys()):
    print(f"{person} {memo[person]}")
