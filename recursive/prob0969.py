"""
给定数组 A，我们可以对其进行煎饼翻转：我们选择一些正整数 k <= A.length，然后反转 A 的前 k 个元素的顺序。我们要执行零次或多次煎饼翻转（按顺序一次接一次地进行）以完成对数组 A 的排序。
返回能使 A 排序的煎饼翻转操作所对应的 k 值序列。任何将数组排序且翻转次数在 10 * A.length 范围内的有效答案都将被判断为正确。
medium

示例 1：

输入：[3,2,4,1]
输出：[4,2,4,3]
解释：
我们执行 4 次煎饼翻转，k 值分别为 4，2，4，和 3。
初始状态 A = [3, 2, 4, 1]
第一次翻转后 (k=4): A = [1, 4, 2, 3]
第二次翻转后 (k=2): A = [4, 1, 2, 3]
第三次翻转后 (k=4): A = [3, 2, 1, 4]
第四次翻转后 (k=3): A = [1, 2, 3, 4]，此时已完成排序。

每次把最大值移动翻转到开头，再翻转到最后
"""
from typing import List


class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:

        def reverse(A: List[int], s, e):
            """
            翻转A，[s, e], 保证参数合法
            """
            while s < e:
                tmp = A[e]
                A[e] = A[s]
                A[s] = tmp
                s += 1
                e -= 1
        ans = []
        def sort_location(A: List[int], idx):
            """
            把A[0:idx) 中最大的放到最后, 并记录翻转步骤到ans中
            """
            if idx <= 1:
                return
            maximum = A[0]
            max_idx = 0
            for i in range(idx):
                if A[i] > maximum:
                    maximum = A[i]
                    max_idx = i
            # 最大的已经在最后了，不用翻转
            if max_idx == idx - 1:
                return
            # 翻转到第一个
            reverse(A, 0, max_idx)
            ans.append(max_idx + 1)
            reverse(A, 0, idx - 1)
            ans.append(idx)
        n = len(A)
        while n > 0:
            sort_location(A, n)
            n -= 1
        return ans


if __name__ == '__main__':
    A = [3,2,4,1]
    sol = Solution()
    print(sol.pancakeSort(A))






