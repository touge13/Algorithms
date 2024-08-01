class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        clockwise rotate
        first reverse up to down, then swap the symmetry 
        1 2 3     7 8 9     7 4 1
        4 5 6  => 4 5 6  => 8 5 2
        7 8 9     1 2 3     9 6 3
        """
        i = 0
        j = len(matrix) - 1
        while i < j:
            matrix[i], matrix[j] = matrix[j], matrix[i]
            i += 1
            j -= 1
        
        for i in range(len(matrix)):    
            for j in range(i + 1, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        return matrix

        """
        anticlockwise rotate
        first reverse left to right, then swap the symmetry
        1 2 3     3 2 1     3 6 9
        4 5 6  => 6 5 4  => 2 5 8
        7 8 9     9 8 7     1 4 7
        """
