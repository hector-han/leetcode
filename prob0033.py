"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
You are given a target value to search. If found in the array return its index, otherwise return -1.
You may assume no duplicate exists in the array.
Your algorithm's runtime complexity must be in the order of O(log n).
"""
from typing import List
import unittest


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        list_len = len(nums)
        if list_len == 0:
            return -1
        i = 0
        j = list_len - 1
        while i < j:
            mid = (i + j) // 2
            if nums[mid] == target:
                return mid

            # 想办法确认target在前半段还是后半段
            if mid == i:
                # 在后半段
                i = mid + 1
            elif nums[mid] > nums[j]:
                # 前半段有序
                if nums[mid] > target >= nums[i]:
                    j = mid - 1
                else:
                    i = mid + 1
            else:
                # 后半段有序
                if nums[mid] < target <= nums[j]:
                    i = mid + 1
                else:
                    j = mid - 1

        if nums[i] == target:
            return i
        return -1


class thisTest(unittest.TestCase):
    def test_case_1(self):
        solution = Solution()
        nums = [4,5,6,7,0,1,2]
        target = 0
        self.assertEqual(solution.search(nums, target), 4)

    def test_case_2(self):
        solution = Solution()
        nums = [4,5,6,7,0,1,2]
        target = 3
        self.assertEqual(solution.search(nums, target), -1)


if __name__ == '__main__':
    unittest.main()
