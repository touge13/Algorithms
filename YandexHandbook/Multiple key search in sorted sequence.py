def binarySearch(n, nums, q):
    l, r = 0, n - 1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == q:
            return mid
        elif nums[mid] > q:
            r = mid - 1
        else:
            l = mid + 1
    return -1

n = int(input())
nums = list(map(int, input().split()))
t = int(input())
targets = list(map(int, input().split()))
for q in targets:
    print(binarySearch(n, nums, q))
