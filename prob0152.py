"""
给定一个整数数组 nums ，找出一个序列中乘积最大的连续子序列（该序列至少包含一个数）。
输入: [2,3,-2,4]
输出: 6

思路，dp
"""

from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        largest[i]表示以i结束的乘积最大的连续子序列
        smallest[i]表示以i结束的乘积最小的(负数)的连续字序列
        """
        length = len(nums)
        largest = [0] * length
        smallest = [0] * length
        largest[0] = nums[0]
        smallest[0] = nums[0]
        ans = largest[0]
        for i in range(1, length):
            cad = [nums[i], largest[i-1]*nums[i], smallest[i-1]*nums[i]]
            largest[i] = max(cad)
            smallest[i] = min(cad)
            if largest[i] > ans:
                ans = largest[i]
        return ans


if __name__ == '__main__':
    sol = Solution()
    nums = [-2,0,-1]
    print(sol.maxProduct(nums))
