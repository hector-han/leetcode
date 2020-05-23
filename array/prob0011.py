"""
11. 盛最多水的容器
medium

给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

输入：[1,8,6,2,5,4,8,3,7]
输出：49

双指针，两边向中心移动，每次移动短的那根。因为，如果当前不是最大的，那么移动长的那根，更不可能是最大的。这就相当于剪枝了。
"""
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        length = len(height)
        if length == 0:
            return 0
        left = 0
        right = length - 1
        ans = 0
        while left < right:
            if height[left] < height[right]:
                ans = max(ans, height[left] * (right - left))
                left += 1
            else:
                ans = max(ans, height[right] * (right - left))
                right -= 1
        return ans


if __name__ == '__main__':
    sol = Solution()
    height = [1,8,6,2,5,4,8,3,7]
    print(sol.maxArea(height))