def number_of_pairs_with_difference_k(nums, k):
    res = 0
    r = 0
    for l in range(len(nums)):
        while r < len(nums) and nums[r] - nums[l] <= k:
            r += 1
        res += len(nums) - r
    return res

n, k = map(int, input().split())
nums = list(map(int, input().split()))
print(number_of_pairs_with_difference_k(nums, k))