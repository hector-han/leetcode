"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Determine if you are able to reach the last index.
"""

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        先计算出每个位置最大能跳到的边界，然后从最后一个开始往前倒推，检查是否可以跳到
        :param nums:
        :return:
        """
        length = len(nums)
        if length <= 1:
            return True

        max_position = [i + nums[i] for i in range(length)]
        idx = length - 2
        threshold = length - 1
        while idx >= 0:
            if max_position[idx] < threshold:
                # 无法到达，考虑前一个
                idx -= 1
                continue
            else:
                if idx == 0:
                    return True
                threshold = idx
                idx = threshold - 1

        return False


if __name__ == '__main__':
    sol = Solution()
    nums = [2,3,1,1,4]
    assert sol.canJump(nums)

    nums = [3,2,1,0,4]
    assert not sol.canJump(nums)