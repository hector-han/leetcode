"""
354. 俄罗斯套娃信封问题
hard
给定一些标记了宽度和高度的信封，宽度和高度以整数对形式 (w, h) 出现。当另一个信封的宽度和高度都比这个信封大的时候，这个信封就可以放进另一个信封里，如同俄罗斯套娃一样。

请计算最多能有多少个信封能组成一组“俄罗斯套娃”信封（即可以把一个信封放到另一个信封里面）。

说明:
不允许旋转信封。

示例:

输入: envelopes = [[5,4],[6,4],[6,7],[2,3]]
输出: 3
解释: 最多信封的个数为 3, 组合为: [2,3] => [5,4] => [6,7]。

先按照w从小到大排序，w相同，按照h从大到小排序。如此，可以对h求最长递增子序列，得到答案

"""
from typing import List


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:

        def longest_increse_seq(nums: List[int]):
            """
            求最长递增子序列长度，仿照纸牌游戏,牌堆个数就是答案
            """
            length = len(nums)
            top = [0] * length
            piles = 0
            for n in nums:
                # 寻找放置的位置 [l, r)
                left = 0
                right = piles
                while left < right:
                    mid = (left + right) // 2
                    if top[mid] < n:
                        left = mid + 1
                    else:
                        right = mid
                if left == piles:
                    top[piles] = n
                    piles += 1
                else:
                    top[left] = n
            return piles
        sorted_evn = sorted(envelopes, key=lambda x: (x[0], -x[1]))
        return longest_increse_seq([e[1] for e in sorted_evn])


if __name__ == '__main__':
    sol = Solution()
    envelopes = [[5, 4], [6, 4], [6, 7], [2, 3]]
    assert sol.maxEnvelopes(envelopes) == 3




