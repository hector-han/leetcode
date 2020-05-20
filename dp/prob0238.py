"""
除自身以外数组的乘积
medium

给你一个长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，其中 output[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。

输入: [1,2,3,4]
输出: [24,12,8,6]
"""
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        定义一个前缀和和后缀和数组
        """
        n = len(nums)
        ans = [0] * n
        prefix = [1] * (n + 1)
        suffix = [1] * n

        for i in range(n-1, 0, -1):
            suffix[i-1] = suffix[i] * nums[i]

        for i in range(n):
            prefix[i + 1] = prefix[i] * nums[i]
            ans[i] = prefix[i] * suffix[i]
        return ans


if __name__ == '__main__':
    sol = Solution()
    nums = [1,2,3,4]
    print(sol.productExceptSelf(nums))