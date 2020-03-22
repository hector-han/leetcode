"""
无重叠区间
medium

给定一个区间的集合，找到需要移除区间的最小数量，使剩余区间互不重叠。

注意:
可以认为区间的终点总是大于它的起点。
区间 [1,2] 和 [2,3] 的边界相互“接触”，但没有相互重叠。

输入: [ [1,2], [2,3], [3,4], [1,3] ]
输出: 1
解释: 移除 [1,3] 后，剩下的区间没有重叠。


按照右端点排序，从小到大选择。

"""

from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        sorted_intervals = sorted(intervals, key=lambda x: x[1])
        num_selected = 0
        n = len(sorted_intervals)
        if n == 0:
            return 0
        last_right = sorted_intervals[0][0] - 1
        for interval in sorted_intervals:
            if interval[0] >= last_right:
                num_selected += 1
                last_right = interval[1]
        return n - num_selected


if __name__ == '__main__':
    # intervals = [ [1,2], [2,3], [3,4], [1,3] ]
    intervals = [[1,100],[11,22],[1,11],[2,12]]
    sol = Solution()
    print(sol.eraseOverlapIntervals(intervals))


