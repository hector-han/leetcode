"""
Given a set of distinct integers, nums, return all possible subsets (the power set).
"""
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # 方式1
        # n = len(nums)
        # ret = [[]]
        # for i in range(n):
        #     tmp = [e + [nums[i]] for e in ret]
        #     ret = ret + tmp
        # return ret

        #方式2
        def backtrack(first=0, curr=[]):
            # if the combination is done
            if len(curr) == k:
                output.append(curr[:])
            for i in range(first, n):
                # add nums[i] into the current combination
                curr.append(nums[i])
                # use next integers to complete the combination
                backtrack(i + 1, curr)
                # backtrack
                curr.pop()

        output = []
        n = len(nums)
        for k in range(n + 1):
            backtrack()
        return output


if __name__ == '__main__':
    nums = [1,2,3]
    sol = Solution()
    print(sol.subsets(nums))