class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}
        for i in nums:
            hm[i] = 1 + hm.get(i, 0)

        a = [[] for _ in range((len(nums) + 1))]
        # частота = индексу числа в массиве a
        for i, j in hm.items():
            a[j].append(i)
        
        res = []
        for i in range(len(a) - 1, 0, -1):
            for j in a[i]:
                res.append(j)
                if len(res) == k:
                    return res
