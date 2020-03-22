"""
最长上升子序列，给定一个未排序的整数数组，找到最长递增子序列的个数。

medium
输入: [10,9,2,5,3,7,101,18]
输出: 4
解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。

说明:
可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
你算法的时间复杂度应该为 O(n2) 。
进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗?

1、递归，dp[i] 表示以nums[i]结尾的最长上升子序列。则dp[i+1] = max(dp[j], where j<i+1, and nums[j] < nums[i+1])
2、分成牌堆。如果当前比所有牌堆下（顶）部都大，新开牌堆，否则防止在最左边的合法位置（下部）。
[10,9,2,5,3,7,101,18] -> 的牌堆
10  5   7   101
9   3       18
2
"""

from typing import List


class Solution1:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        length = len(nums)
        dp = [0] * length
        dp[0] = 1
        ans = 1
        for i in range(1, len(nums)):
            j = 0
            tmp = 0
            while j < i:
                if nums[j] < nums[i]:
                    tmp = max(tmp, dp[j])
                j += 1
            ans = max(tmp + 1, ans)
            dp[i] = tmp + 1
        return ans


class Solution2:
    def lengthOfLIS(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 0:
            return 0
        heap = []
        for num in nums:
            # find location, 牌堆顶是有序的
            begin = 0
            end = len(heap)

            while begin < end:
                mid = (begin + end) // 2
                if heap[mid] == num:
                    begin = mid
                    break
                elif heap[mid] > num:
                    end = mid
                else:
                    begin = mid + 1
            if begin < len(heap):
                heap[begin] = num
            else:
                heap.append(num)

        return len(heap)


if __name__ == '__main__':
    nums = [10,9,2,5,3,7,101,18]
    sol = Solution2()
    print(sol.lengthOfLIS(nums))


