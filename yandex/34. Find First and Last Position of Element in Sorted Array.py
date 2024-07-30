class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        i = j = -1

        l = 0
        r = len(nums) - 1
        # search for the left one
        while l <= r:
            mid = (l + r) // 2
            if target <= nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
            if nums[mid] == target:
                i = mid

        l = 0
        r = len(nums) - 1
        # search for the right one
        while l <= r:
            mid = (l + r) // 2
            if target >= nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
            if nums[mid] == target:
                j = mid
        return [i, j]
