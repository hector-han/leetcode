"""
Given an unsorted integer array, find the smallest missing positive integer.
"""

from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        哪个数字出现过，就把它设置个标记
        一般需要额外的存储空间，但是数组下标本身可以作为数字，数组中值可以作为是否出现的标志
        如果i-1位置上存储的值刚好是i,那么说明i出现过。
        :param nums:
        :return:
        """
        length = len(nums)
        for i in range(length):
            # num 出现过，设置num-1位置的值为num。 需要缓存num-1位置原来的值，存储到nums[num-1] - 1上...
            # 如果不在范围内，即可停止。如果一直在范围内，必然有一个环。
            num = nums[i]
            while 0 <= num - 1 < length and nums[num - 1] != num:
                tmp = nums[num - 1]
                nums[num - 1] = num
                num = tmp
        for i in range(length):
            if nums[i] != i + 1:
                return i + 1
        return length + 1


if __name__ == '__main__':
    sol = Solution()
    nums = [1,2,0]
    assert sol.firstMissingPositive(nums) == 3
    nums = [3,4,-1,1]
    assert sol.firstMissingPositive(nums) == 2
    nums = [7,8,9,11,12]
    assert sol.firstMissingPositive(nums) == 1
