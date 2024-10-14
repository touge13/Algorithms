# a = {1, 2, 3}
# b = {3, 4, 5}
# result = a | b  # {1, 2, 3, 4, 5}
# result = a & b  # {3}
# result = a - b  # {1, 2}
# result = a ^ b  # {1, 2, 4, 5}

q = int(input())
s = set()

for _ in range(q):
    action, num = map(int, input().split())
    if action == 1:
        s.add(num)
    elif action == 2:
        if num in s:
            print(1)
        else:
            print(0)
