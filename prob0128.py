"""
给定一个未排序的整数数组，找出最长连续序列的长度。
要求算法的时间复杂度为 O(n)。
"""
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        cache = set()
        max_len = 0
        for num in nums:
            cache.add(num)
        for num in nums:
            if num - 1 in cache:
                continue
            i = 1
            while num + i in cache:
                i += 1
            max_len = max(max_len, i)
        return max_len