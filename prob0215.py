"""
在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
medium

输入: [3,2,1,5,6,4] 和 k = 2
输出: 5

类似快排的思路，把数组分为两部分，然后检查两部分的元素个数
"""

from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partiton(start, end, k):
            #[start, end)
            if start == end - 1:
                assert k == 1
                return nums[start]
            i, j = start, end - 1
            stash = nums[start]
            while i < j:
                while i < j and nums[j] <= stash:
                    j -= 1
                nums[i] = nums[j]

                while i < j and nums[i] >= stash:
                    i += 1
                nums[j] = nums[i]
            nums[i] = stash

            if i - start == k - 1:
                return nums[i]
            elif i - start < k - 1:
                return partiton(i+1, end, k - (i-start+1))
            else:
                return partiton(start, i, k)

        return partiton(0, len(nums), k)

if __name__ == '__main__':
    nums =  [3,2,1,5,6,4]
    k = 2
    nums = [3,2,3,1,2,4,5,5,6]
    k = 4
    sol = Solution()
    print(sol.findKthLargest(nums, k))
