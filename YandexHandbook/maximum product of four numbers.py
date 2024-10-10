n = int(input())
nums = map(int, input().split())

max1 = max2 = max3 = max4 = float('-inf')
min1 = min2 = min3 = min4 = float('inf')

for i in nums:
    if i >= max1:
        max4 = max3
        max3 = max2
        max2 = max1
        max1 = i
    elif i >= max2:
        max4 = max3
        max3 = max2
        max2 = i
    elif i >= max3:
        max4 = max3
        max3 = i
    elif i >= max4:
        max4 = i

    if i <= min1:
        min4 = min3
        min3 = min2
        min2 = min1
        min1 = i
    elif i <= min2:
        min4 = min3
        min3 = min2
        min2 = i
    elif i <= min3:
        min4 = min3
        min3 = i
    elif i <= min4:
        min4 = i
        
a = max1 * max2 * max3 * max4
b = min1 * min2 * max1 * max2
d = min1 * min2 * min3 * min4

print(max(a, b, d))
