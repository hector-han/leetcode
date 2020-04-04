"""
滑动窗口最大值
hard

给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。
返回滑动窗口中的最大值。

输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
输出: [3,3,5,5,6,7]
解释:

  滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
"""

from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        单调队列，队列头的是最大的元素。窗口滑动时，右边的入队，左边的出队，出队时判断。
        :return:
        """
        queue = []

        def push(v):
            while queue and queue[-1] < v:
                queue.pop()
            queue.append(v)

        n = len(nums)
        ans = []
        for i in range(n):
            if i < k - 1:
                push(nums[i])
            else:
                push(nums[i])
                ans.append(queue[0])
                v = nums[i-k+1]
                if queue[0] == v:
                    queue.pop(0)
        return ans


if __name__ == '__main__':
    nums = [-7,-8,7,5,7,1,6,0]
    k = 4
    sol = Solution()
    print(sol.maxSlidingWindow(nums, k))