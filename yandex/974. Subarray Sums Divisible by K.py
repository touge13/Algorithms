class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        d = {0:1} 
        prefixSum = res = 0
        for n in nums:
            prefixSum += n
            if prefixSum % k in d:
                res += d[prefixSum % k]
            d[prefixSum % k] = 1 + d.get(prefixSum % k, 0)
        return res

# мы можем находить раницу префиксных сумм: [1,2,3,4] - [1,2] (тут делится на 7)
