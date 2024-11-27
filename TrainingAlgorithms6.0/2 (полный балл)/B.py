def count_subarrays_with_sum_k(nums, K):
    res = 0
    prefixSum = 0
    d = {0: 1}
    for n in nums:
        prefixSum += n
        if prefixSum - K in d:
            res += d[prefixSum - K]
        d[prefixSum] = 1 + d.get(prefixSum, 0)
    return res

N, K = map(int, input().split())
nums = list(map(int, input().split()))
print(count_subarrays_with_sum_k(nums, K))
