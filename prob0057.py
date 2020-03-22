"""
插入区间
hard

给出一个无重叠的 ，按照区间起始端点排序的区间列表。
在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。

输入: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
输出: [[1,2],[3,10],[12,16]]
解释: 这是因为新的区间 [4,8] 与 [3,5],[6,7],[8,10] 重叠。

"""

from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        left = []
        min_l = newInterval[0]
        max_r = newInterval[1]
        right = []

        for v in intervals:
            if v[1] < newInterval[0]:
                left.append(v)
            elif v[0] > newInterval[1]:
                right.append(v)
            else:
                min_l = min(min_l, v[0])
                max_r = max(max_r, v[1])

        return left + [[min_l, max_r]] + right


if __name__ == '__main__':
    intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
    newInterval = [4, 8]
    sol = Solution()
    print(sol.insert(intervals, newInterval))