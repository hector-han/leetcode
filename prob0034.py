"""
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
Your algorithm's runtime complexity must be in the order of O(log n).
If the target is not found in the array, return [-1, -1].
"""

from typing import List

class Solution:
    """
    while 循环使用 start -1 < end， 可以确保不会死循环，跳出循环时，只有两个元素未检查
    """
    def searchFirst(self, nums: List[int], target: int) -> int:
        length = len(nums)
        start, end = 0, length - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid
            else:
                end = mid
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1

    def searchLast(self, nums: List[int], target: int) -> int:
        length = len(nums)
        start, end = 0, length - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] > target:
                end = mid
            else:
                start = mid
        if nums[end] == target:
            return end
        if nums[start] == target:
            return start
        return -1

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        if length == 0:
            return [-1, -1]
        return [self.searchFirst(nums, target), self.searchLast(nums, target)]


if __name__ == '__main__':
    sol = Solution()
    assert sol.searchRange([5,7,7,8,8,10], 8) == [3, 4]
    assert sol.searchRange([5,7,7,8,8,10], 6) == [-1, -1]