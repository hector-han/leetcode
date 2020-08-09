"""
给定一个m*n的矩阵，里面每个元素都是非负数（不妨设都大于1),求从左上角到右下角的最小代价路径，代价为路径走过的数字之和。
1、dijstra算法。 不要急着想算法，慢慢从最简单情况开始。
2、A*, A*需要保证 从中间节点到目标节点的预估距离，小于真实代价。
see https://zhuanlan.zhihu.com/p/113008274
"""
import numpy as np
from typing import List
from queue import PriorityQueue


class Solution1:
    def shortestPath(self, matrix: List[List[int]]):
        m = len(matrix)
        n = len(matrix[0])
        def _get(point):
            return matrix[point[0]][point[1]]

        def _neighber(p):
            x = p[0]
            y = p[1]
            ans = []
            for offset in [-1, 1]:
                if 0 <= y + offset < n:
                    ans.append((x, y+offset))
                if 0 <= x + offset < m:
                    ans.append((x+offset, y))
            return ans

        start = (0, 0)
        end = (m-1, n-1)
        frontier = PriorityQueue()
        frontier.put((_get(start), start))
        dict_cost = dict()
        dict_from = dict()
        dict_cost[start] = _get(start)
        dict_from[start] = None

        while not frontier.empty():
            cur = frontier.get()[1]
            if cur == end:
                break
            for p in _neighber(cur):
                new_cost = dict_cost[cur] + _get(p)
                if p not in dict_cost or new_cost < dict_cost[p]:
                    dict_cost[p] = new_cost
                    frontier.put((new_cost, p))
                    dict_from[p] = cur
        return dict_cost[end]



class Solution2:
    def shortestPath(self, matrix: List[List[int]]):
        m = len(matrix)
        n = len(matrix[0])
        def _get(point):
            return matrix[point[0]][point[1]]

        def _neighber(p):
            x = p[0]
            y = p[1]
            ans = []
            for offset in [-1, 1]:
                if 0 <= y + offset < n:
                    ans.append((x, y+offset))
                if 0 <= x + offset < m:
                    ans.append((x+offset, y))
            return ans

        def _h(p):
            x = p[0]
            y = p[1]
            return abs(m-1-x) + abs(n-1-y)

        start = (0, 0)
        end = (m-1, n-1)
        frontier = PriorityQueue()
        frontier.put((_get(start), start))
        dict_cost = dict()
        dict_from = dict()
        dict_cost[start] = _get(start)
        dict_from[start] = None

        while not frontier.empty():
            cur = frontier.get()[1]
            if cur == end:
                break
            for p in _neighber(cur):
                new_cost = dict_cost[cur] + _get(p)
                if p not in dict_cost or new_cost < dict_cost[p]:
                    dict_cost[p] = new_cost
                    frontier.put((new_cost + _h(p), p))
                    dict_from[p] = cur
        return dict_cost[end]



if __name__ == '__main__':
    matirx = np.random.randint(1, 20, (3, 5))
    sol1 = Solution1()
    print(sol1.shortestPath(matirx))
    sol2 = Solution2()
    print(sol2.shortestPath(matirx))








