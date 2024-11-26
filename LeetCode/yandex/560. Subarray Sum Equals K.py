class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = 0
        hashTable = {0:1}
        res = 0
        for num in nums:
            prefixSum += num
            if (prefixSum - k) in hashTable:
                res += hashTable[prefixSum - k]
            if prefixSum in hashTable:
                hashTable[prefixSum] += 1
            else: 
                hashTable[prefixSum] = 1
        return res
            