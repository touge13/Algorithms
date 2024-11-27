n = int(input())
lst = list(map(int, input().split()))
res = [0] * n
prefixSum = 0
for i in range(len(lst)):
    prefixSum += lst[i]
    res[i] = prefixSum
print(*res)