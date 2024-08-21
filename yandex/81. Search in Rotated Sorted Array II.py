class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return True

            '''
            Единственное отличие от 33. Search in Rotated Sorted Array в том, что из-за существования дубликатов 
            у нас может быть nums[left] == ​​nums[mid], и в этом случае первая 
            половина может быть не в порядке возрастания ([3 1 2 3 3 3 3]). 
            В этом случае гарантированно, вся правая часть nums[mid:r+1] состоит из 
            чисел nums[l] (оно же равно nums[mid] и nums[r]), поэтому, будем смещать наш 
            левый указатель направо, пока nums[l] перестанет быть равным nums[mid].
            '''

            while l < mid and nums[l] == nums[mid]:
                l += 1

            if nums[l] <= nums[mid]:
                if nums[l] <= target <= nums[mid]:
                    r = mid
                else:
                    l = mid + 1
            else:
                if nums[mid] <= target <= nums[r]:
                    l = mid
                else:
                    r = mid - 1
        return False
