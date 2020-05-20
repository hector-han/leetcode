"""
移动0
easy

给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

示例:
输入: [0,1,0,3,12]
输出: [1,3,12,0,0]

说明:

必须在原数组上操作，不能拷贝额外的数组。
尽量减少操作次数。
"""
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        记录第一个0的位置，和第一个非零的位置，直到第一个非零位置的指针到达末尾
        """
        def swap(i, j):
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp

        first_zero = 0
        length = len(nums)
        while first_zero < length and nums[first_zero] != 0:
                first_zero += 1
        if first_zero == length:
            #都不为0
            return
        first_no_zero = first_zero + 1
        while first_no_zero < length:
            while nums[first_no_zero] == 0:
                first_no_zero += 1
                if first_no_zero == length:
                    return
            swap(first_zero, first_no_zero)

            first_zero += 1
            first_no_zero += 1


if __name__ == '__main__':
    sol = Solution()
    nums = [0, 1, 0, 0, 3]
    sol.moveZeroes(nums)
    print(nums)




