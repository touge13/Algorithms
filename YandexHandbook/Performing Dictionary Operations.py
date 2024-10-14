# dict1 = {'a': 1, 'b': 2}
# dict2 = {'b': 3, 'c': 4}
# result = dict1 | dict2  # {'a': 1, 'b': 3, 'c': 4}
# dict1 |= dict2  # dict1 становится {'a': 1, 'b': 3, 'c': 4}

# dict1 = {'a': 1, 'b': 2, 'c': 3}
# dict2 = {'b': 3, 'c': 4}
# result = dict1 - dict2  # {'a': 1}
# dict1 -= dict2  # dict1 становится {'a': 1}

d = {}
q = int(input())
for _ in range(q):
    userInput = list(map(int, input().split()))
    if len(userInput) == 3:
        d[userInput[1]] = userInput[2]
    elif len(userInput) == 2:
        if userInput[1] in d:
            print(d[userInput[1]])
        else:
            print(-1)
