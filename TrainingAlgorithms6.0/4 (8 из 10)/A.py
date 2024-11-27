def find_height(name, parent_dict, height_dict):
    if name not in height_dict:
        parent = parent_dict[name]
        height_dict[name] = find_height(parent, parent_dict, height_dict) + 1
    return height_dict[name]

def create_tree(parent_dict):
    height_dict = {}
    
    all_people = set(parent_dict.keys()) | set(parent_dict.values())
    root = (all_people - set(parent_dict.keys())).pop()
    height_dict[root] = 0
    
    for person in all_people:
        if person not in height_dict:
            find_height(person, parent_dict, height_dict)

    for name in sorted(height_dict.keys()):
        print(name, height_dict[name])

N = int(input())
parent_dict = {}
for _ in range(N - 1):
    child, parent = input().split()
    parent_dict[child] = parent
create_tree(parent_dict)