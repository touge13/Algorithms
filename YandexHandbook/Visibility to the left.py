n = int(input())
nums = list(map(int, input().split()))
stack = []
res = [0] * n

for i in range(n):
    while stack and nums[i] > stack[-1][0]:
        elem, num = stack.pop()
        res[i] += res[num] + 1
    stack.append((nums[i], i))
    
print(*res)
