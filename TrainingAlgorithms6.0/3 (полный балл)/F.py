def find_minimum_PSP(n, w, s):
    order = {w[i]: i for i in range(4)}
    d = {'(':')', '[':']'}
    stack = []
    result = list(s)

    for ch in s:
        if ch in d:
            stack.append(ch)
        elif ch in d.values():
            if stack and d[stack[-1]] == ch:
                stack.pop()
            else:
                return "" 

    def complete_PSP():
        min_open = min("([", key=lambda x: order[x])

        while len(result) + len(stack) < n:
            if stack:        
                if order[d[stack[-1]]] > order[min_open]:
                    result.append(min_open)
                    stack.append(min_open)
                else:
                    result.append(d[stack.pop()])
            else:
                result.append(min_open) 
                stack.append(min_open) 

        while stack:
            result.append(d[stack.pop()])

        return ''.join(result)
    return complete_PSP()

n = int(input())
w = input().strip()
s = input().strip()
print(find_minimum_PSP(n, w, s))
