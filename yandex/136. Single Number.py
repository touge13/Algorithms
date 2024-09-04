class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res ^= num
        return res
        
"""
a = 5  # В двоичной системе: 0101
b = 3  # В двоичной системе: 0011

result = a ^ b
print(result)  # Вывод: 6 (в двоичной системе: 0110)
"""
