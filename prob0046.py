"""
Given a collection of distinct integers, return all possible permutations.
"""
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        递归， 先固定一个，后面几个permute
        :param nums:
        :return:
        """
        length = len(nums)
        if length == 0:
            return [[]]
        if length == 1:
            return [nums]

        ret = []
        for i in range(length):
            cur = nums[i]
            left_list = nums[0:i] + nums[i+1:length]
            tmp = self.permute(left_list)
            for ele in tmp:
                ret.append([cur] + ele)
        return ret


if __name__ == '__main__':
    sol = Solution()
    nums = [1, 2, 3]
    ans = sol.permute(nums)
    print(ans)