
"""
Input:
[1, 2, 3]
[4, 5, 6]
[7, 8, 9]

Transpose:
row_idx = 0 col_idx = 0     row_idx = 0 col_idx = 1     row_idx = 0 col_idx = 2
[1, 2, 3]                   [1, 4, 3]                   [1, 4, 7]
[4, 5, 6]                   [2, 5, 6]                   [2, 5, 6]
[7, 8, 9]                   [7, 8, 9]                   [3, 8, 9]

row_idx = 1 col_idx = 1     row_idx = 1 col_idx = 2
[1, 4, 7]                   [1, 4, 7]
[2, 5, 6]                   [2, 5, 8]
[3, 8, 9]                   [3, 6, 9]

Reverse:
row_idx = 0 col_idx = 1
[1, 4, 7]
[2, 5, 8]
[3, 6, 9]

"""


class Solution(object):
    def rotate(self, matrix):
        """
        Transpose diagonally then Reverse Left to right
        O(M) - time complexity, where M is the matrix size
        O(1) - space complexity
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        height = len(matrix)
        for row_idx in range(height):
            for column_idx in range(row_idx, height):
                matrix[row_idx][column_idx], matrix[column_idx][row_idx] = matrix[column_idx][row_idx], matrix[row_idx][column_idx]
        for row_idx in range(height):
            for column_idx in range(height // 2):
                matrix[row_idx][column_idx], matrix[row_idx][-column_idx-1] = matrix[row_idx][-column_idx-1], matrix[row_idx][column_idx]
        return matrix


if __name__ == '__main__':
    s = Solution()
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    output = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    assert s.rotate(matrix) == output
    matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    output = [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]
    assert s.rotate(matrix) == output
