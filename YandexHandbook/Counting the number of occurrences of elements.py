def binarySearchMin(n, nums, q):
    minIndex = -1
    l, r = 0, n - 1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == q:
            minIndex = mid
            r = mid - 1
        elif nums[mid] > q:
            r = mid - 1
        else:
            l = mid + 1
    return minIndex

def binarySearchMax(n, nums, q):
    maxIndex = -1
    l, r = 0, n - 1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == q:
            maxIndex = mid
            l = mid + 1
        elif nums[mid] > q:
            r = mid - 1
        else:
            l = mid + 1
    return maxIndex

n = int(input())
nums = list(map(int, input().split()))
t = int(input())
targets = list(map(int, input().split()))
res = []
for q in targets:
    minIndex = binarySearchMin(n, nums, q)
    if minIndex == -1:
        res.append(0)
    else:
        maxIndex = binarySearchMax(n, nums, q)
        res.append(maxIndex - minIndex + 1)
print(*res)
