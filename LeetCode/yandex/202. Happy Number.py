# logn 
class Solution:
    def isHappy(self, n: int) -> bool:
        d = {}
        while n != 1:
            chars = [int(n) for n in str(n)]
            temp = 0
            for i in chars:
                temp += i ** 2
            if temp in d:
                return False
            else:
                d[temp] = 1
            n = temp
        return True 
