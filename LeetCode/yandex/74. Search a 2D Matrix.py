class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ln = 0
        rn = len(matrix) - 1
        while ln <= rn:
            midn = (ln + rn) // 2
            if matrix[midn][0] <= target <= matrix[midn][-1]:
                lm = 0
                rm = len(matrix[midn]) - 1
                while lm <= rm:
                    midm = (lm + rm) // 2
                    if matrix[midn][midm] == target:
                        return True
                    elif matrix[midn][midm] < target:
                        lm = midm + 1
                    elif matrix[midn][midm] > target:
                        rm = midm - 1
                return False
            elif matrix[midn][-1] < target:
                ln = midn + 1
            elif matrix[midn][0] > target:
                rn = midn - 1
        return False
