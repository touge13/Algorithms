class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        square = 0
        r = len(height) - 1
        while l < r:
            square = max(square, min(height[l], height[r]) * (r - l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return square
