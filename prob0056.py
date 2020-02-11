"""
Given a collection of intervals, merge all overlapping intervals.
"""
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        def overlap(interval1, interval2):
            if interval1[1] < interval2[0]:
                return False
            return True

        # 按照左端点又小到大排序
        intervals = sorted(intervals, key=lambda x: x[0])
        ret = []
        if len(intervals) == 0:
            return intervals
        cur = intervals[0]
        for interval in intervals[1:]:
            if overlap(cur, interval):
                cur = [cur[0], max(cur[1], interval[1])]
            else:
                ret.append(cur)
                cur = interval
        ret.append(cur)

        return ret

if __name__ == '__main__':
    sol = Solution()
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    print(sol.merge(intervals))
    intervals = [[1,4],[4,5]]
    print(sol.merge(intervals))
