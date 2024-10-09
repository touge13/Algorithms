class Solution:
    def minSwaps(self, s: str) -> int:
        stackSize = 0
        for ch in s:
            if ch == '[':
                stackSize += 1
            else:
                if stackSize > 0:
                    stackSize -= 1
        return int((stackSize + 1) / 2)
