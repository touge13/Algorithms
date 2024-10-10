n = int(input())
nums = map(int, input().split())

max1 = -1
max2 = -1

for i in nums:
    if i >= max1:
        max2 = max1
        max1 = i
    elif i >= max2:
        max2 = i

print(max1 * max2)