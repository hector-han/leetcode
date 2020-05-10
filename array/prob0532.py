"""
数组中的K-diff数对
easy
给定一个整数数组和一个整数 k, 你需要在数组里找到不同的 k-diff 数对。这里将 k-diff 数对定义为一个整数对 (i, j), 其中 i 和 j 都是数组中的数字，且两数之差的绝对值是 k.

示例 1:

输入: [3, 1, 4, 1, 5], k = 2
输出: 2
解释: 数组中有两个 2-diff 数对, (1, 3) 和 (3, 5)。
尽管数组中有两个1，但我们只应返回不同的数对的数量。
"""
from typing import List


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        # 记录元素出现的次数
        if k < 0:
            return 0
        cache = {}
        for n in nums:
            if n in cache:
                cache[n] += 1
            else:
                cache[n] = 1
        # 只找其中大于的个数
        ans = 0
        for n in cache:
            if n + k in cache:
                if k == 0:
                    if cache[n] > 1:
                        ans += 1
                else:
                    ans += 1

        return ans


if __name__ == '__main__':
    sol = Solution()
    nums = [3, 1, 4, 1, 5]
    k = 2
    print(sol.findPairs(nums, k))


