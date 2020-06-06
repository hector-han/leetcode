"""
给定一个m*n的矩阵，里面每个元素都是非负数（不妨设都大于1),求从左上角到右下角的最小代价路径，代价为路径走过的数字之和。
1、dijstra算法。
2、A*, A*需要保证 从中间节点到目标节点的预估距离，小于真实代价。
see https://zhuanlan.zhihu.com/p/113008274
"""
from typing import List
from queue import PriorityQueue


class Solution1:
    def shortestPath(self, matrix: List[List[int]]):
        m = len(matrix)
        n = len(matrix[0])







