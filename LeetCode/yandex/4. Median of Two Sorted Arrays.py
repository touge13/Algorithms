#сложность O(n + m), решение двумя указателями

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        list = []
        i = j = 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                list.append(nums1[i])
                i += 1
            else:
                list.append(nums2[j])
                j += 1

        while i < len(nums1):
            list.append(nums1[i])
            i += 1

        while j < len(nums2):
            list.append(nums2[j])
            j += 1

        if len(list) % 2 == 0:
            return (list[len(list) // 2 - 1] + list[len(list) // 2]) / 2
        else: 
            return list[len(list) // 2]  