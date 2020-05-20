"""
找到所有数组中消失的数字
easy

给定一个范围在  1 ≤ a[i] ≤ n ( n = 数组大小 ) 的 整型数组，数组中的元素一些出现了两次，另一些只出现一次。
找到所有在 [1, n] 范围之间没有出现在数组中的数字。
您能在不使用额外空间且时间复杂度为O(n)的情况下完成这个任务吗? 你可以假定返回的数组不算在额外空间内。

数组其实可以看成一个idx->value的map

"""
from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ans = []
        length = len(nums)
        for i in range(length):
            idx = abs(nums[i]) - 1
            # 访问过，就设置为负数
            if nums[idx] > 0:
                nums[idx] = -nums[idx]
        for i in range(length):
            if nums[i] > 0:
                ans.append(i+1)
        return ans


if __name__ == '__main__':
    nums = [4, 3, 2, 7, 7, 2, 3, 1]
    sol = Solution()
    print(sol.findDisappearedNumbers(nums))