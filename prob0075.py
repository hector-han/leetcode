"""
颜色分类
medium
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.
Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
"""
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        目标是分成三段，00000 111111 2222222
        i从前往后，j从后往前。如果i,j里有【0,2】调整到相应位置，看情况调整i,j。
        如果i j都是1，记录最开始和最后的位置，出现0了最开始的对调，出现2了和最初的对调
        """
        length = len(nums)
        last_0_idx = 0
        first_2_idx = length - 1
        i = 0
        def swap(i, j):
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp
        while i <= first_2_idx:
            if nums[i] == 0:
                swap(i, last_0_idx)
                i += 1
                last_0_idx += 1
            elif nums[i] == 2:
                swap(i, first_2_idx)
                first_2_idx -= 1
            else:
                i += 1


if __name__ == '__main__':
    sol = Solution()
    nums = [2,0,2,1,1,0]
    sol.sortColors(nums)
    print(nums)




