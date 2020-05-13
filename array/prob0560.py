"""
 和为K的子数组
 medium
 给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。
 输入:nums = [1,1,1], k = 2
输出: 2 , [1,1] 与 [1,1] 为两种不同的情况。
"""
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        累积和
        """
        leiji_map = {}
        ans = 0
        tmp = 0
        leiji_map[0] = [-1]
        for i in range(len(nums)):
            tmp += nums[i]
            target = tmp - k
            if target in leiji_map:
                ans += len(leiji_map[target])
            if tmp not in leiji_map:
                leiji_map[tmp] = []
            leiji_map[tmp].append(i)
        return ans
