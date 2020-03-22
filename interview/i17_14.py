"""
面试题 17.14. 最小K个数
设计一个算法，找出数组中最小的k个数。以任意顺序返回这k个数均可。

示例：

输入： arr = [1,3,5,7,2,4,6,8], k = 4
输出： [1,2,3,4]

快排思路更直观一点，但是想自己写个堆
大顶堆解决
"""

from typing import List


class Solution:
    def smallestK(self, arr: List[int], k: int) -> List[int]:
        if k == 0:
            return []
        max_heap = [None] * k
        num_heap = 0

        def adjust_heap(heap_list, i, num_heap):
            if num_heap == 1:
                return
            max_idx = i
            left = 2 * i + 1
            right = left + 1

            if left < num_heap and heap_list[left] > heap_list[max_idx]:
                max_idx = left
            if right < num_heap and heap_list[right] > heap_list[max_idx]:
                max_idx = right

            if max_idx != i:
                heap_list[i], heap_list[max_idx] = heap_list[max_idx], heap_list[i]
                adjust_heap(heap_list, max_idx, num_heap)

        for v in arr:
            if num_heap == k:
                if v >= max_heap[0]:
                    continue
                else:
                    max_heap[0] = v
                    adjust_heap(max_heap, 0, num_heap)
            else:
                # 插入堆并调整堆
                max_heap[num_heap] = v
                num_heap += 1
                idx = num_heap // 2 - 1
                while idx >= 0:
                    adjust_heap(max_heap, idx,  num_heap)
                    idx = (idx + 1) // 2 - 1
        return max_heap

if __name__ == '__main__':
    arr = [1, 3, 5, 7, 2, 4, 6, 8]
    k = 4
    sol = Solution()
    print(sol.smallestK(arr, k))






