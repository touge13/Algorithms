def find_min_in_the_window(n, k, nums):
    result = []
    deque = []

    for i in range(n):
        if deque and deque[0] < i - k + 1:
            deque.pop(0)
        while deque and nums[i] <= nums[deque[-1]]:
            deque.pop()
        deque.append(i)
        if i >= k - 1:
            result.append(nums[deque[0]])
    return result 

n, k = map(int, input().split())
nums = list(map(int, input().split()))
result = find_min_in_the_window(n, k, nums)
for r in result:
    print(r)