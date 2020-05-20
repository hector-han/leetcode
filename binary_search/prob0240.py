"""
搜索二维矩阵 II
medium

编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target。该矩阵具有以下特性：

每行的元素从左到右升序排列。
每列的元素从上到下升序排列。

"""

class Solution:
    def searchMatrix(self, matrix, target):
        """
        类似于二分查找，把矩阵分成4块
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        def recursive_search(left_top, right_bottom):
            if left_top[0] > right_bottom[0] or left_top[1] > right_bottom[1]:
                return False

            if left_top == right_bottom:
                if matrix[left_top[0]][left_top[1]] == target:
                    return True
                else:
                    return False
            mid = [(v[0] + v[1]) // 2 for v in zip(left_top, right_bottom)]

            if matrix[mid[0]][mid[1]] == target:
                return True
            elif matrix[mid[0]][mid[1]] < target:
                ans = recursive_search([mid[0]+1, mid[1]+1], right_bottom)

                region_1_left = [mid[0]+1, left_top[1]]
                region_1_right = [right_bottom[0], mid[1]]
                ans1 = recursive_search(region_1_left, region_1_right)

                region_2_left = [left_top[0], mid[1]+1]
                region_2_right = [mid[0], right_bottom[1]]
                ans2 = recursive_search(region_2_left, region_2_right)

                return ans or ans1 or ans2
            else:
                ans = recursive_search(left_top, [mid[0]-1, mid[1]-1])

                region_1_left = [mid[0], left_top[1]]
                region_1_right = [right_bottom[0], mid[1]-1]
                ans1 = recursive_search(region_1_left, region_1_right)

                region_2_left = [left_top[0], mid[1]]
                region_2_right = [mid[0]-1, right_bottom[1]]
                ans2 = recursive_search(region_2_left, region_2_right)

                return ans or ans1 or ans2
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])

        return recursive_search([0, 0], [m-1, n-1])


if __name__ == '__main__':
    sol = Solution()
    matrix = [
      [1,   4,  7, 11, 15],
      [2,   5,  8, 12, 19],
      [3,   6,  9, 16, 22],
      [10, 13, 14, 17, 24],
      [18, 21, 23, 26, 30]
    ]
    print(sol.searchMatrix(matrix, 5))
    print(sol.searchMatrix(matrix, 20))
