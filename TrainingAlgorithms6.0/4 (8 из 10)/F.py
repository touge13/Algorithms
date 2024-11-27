import sys
sys.setrecursionlimit(250000)

def build_tree(managers):
    tree = {}
    for i, manager in enumerate(managers, start=2):
        if manager not in tree:
            tree[manager] = []
        tree[manager].append(i)    
    return tree

def process_employee(tree, employee, coins):
    total_coins = 0
    total_tasks = 1

    if employee not in tree:
        coins[employee - 1] = 1
        return 1, 1

    for subordinate in tree[employee]:
        coins_from_sub, tasks = process_employee(tree, subordinate, coins)
        total_coins += coins_from_sub
        total_tasks += tasks

    total_coins += total_tasks
    coins[employee - 1] = total_coins
    return total_coins, total_tasks

def calculate_coins(n, managers):
    tree = build_tree(managers)
    coins = [0] * n
    process_employee(tree, 1, coins)
    return coins

n = int(input())
if n > 1:
    managers = list(map(int, input().split()))
else:
    managers = []

print(" ".join(map(str, calculate_coins(n, managers))))
