"""
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).
"""
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        想象是一个洋葱，一层一层旋转
        """
        n = len(matrix)
        for lower in range(n // 2):
            # 像洋葱一样，一层rotate
            upper = n - 1 - lower
            stash = [matrix[i][lower] for i in range(lower, upper)]
            # 左边
            for i in range(lower, upper):
                matrix[i][lower] = matrix[upper][i]
            # 下边
            for j in range(lower, upper):
                matrix[upper][j] = matrix[lower + upper - j][upper]
            # 右边
            for i in range(upper, lower, -1):
                matrix[i][upper] = matrix[lower][i]
            # 上边
            for j in range(upper, lower, -1):
                matrix[lower][j] = stash[upper - j]



if __name__ == '__main__':
    sol = Solution()
    matrix = [
      [1,2,3],
      [4,5,6],
      [7,8,9]
    ]
    sol.rotate(matrix)
    print(matrix)
