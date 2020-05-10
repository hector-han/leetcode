"""
最长等差数列
medium

给定一个整数数组 A，返回 A 中最长等差子序列的长度。
回想一下，A 的子序列是列表 A[i_1], A[i_2], ..., A[i_k] 其中 0 <= i_1 < i_2 < ... < i_k <= A.length - 1。并且如果 B[i+1] - B[i]( 0 <= i < B.length - 1) 的值都相同，那么序列 B 是等差的。

输入：[20,1,15,3,10,5,8]
输出：4
解释：
最长的等差子序列是 [20,15,10,5]。
"""
from typing import List


class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        # dp[i][j]，以i开头，以j结尾的，等差数列的个数，不具有动态规划性质，不对
        n = len(A)
        dp = [[0] * n for i in range(n)]
        for i in range(n-1):
            dp[i][i+1] = 2
        for i in range(n-1):
            for j in range(i+1, n):
                # 计算dp[i][j], 枚举k in [i+1, j-1]
                tmp = 2
                for k in range(i+1, j):
                    step1 = (A[k] - A[i]) // (dp[i][k] - 1)
                    # if (A[k] - A[i]) % (dp[i][k] - 1) != 0:
                    #     print('error')
                    step2 = A[j] - A[k]
                    if step1 == step2:
                        if dp[i][k] + 1 > tmp:
                            tmp = dp[i][k] + 1
                dp[i][j] = tmp

        ans = 0
        for i in range(n-1):
            for j in range(i+1, n):
                if dp[i][j] > ans:
                    ans = dp[i][j]
                    print(i, j)
        print(dp[16][37])
        return ans

from collections import defaultdict



class Solution2:
    def longestArithSeqLength(self, A: List[int]) -> int:
        # 建立字典储存A的信息，key是A的数值，val是这个数值的index的列表
        A_mapping = defaultdict(list)
        for i, num in enumerate(A):
            A_mapping[num].append(i)
        max_len = 2
        n = len(A)
        # 两层遍历，对于每个i，j看以A[i],A[j]为前两项的等差数列有几项。
        for i in range(n):
            for j in range(i+1, n):
                d = A[j] - A[i]
                length = 2
                while True:
                    if A[j] + d not in A_mapping:
                        break
                    key = False
                    for k in A_mapping[A[j] + d]:
                        if k > j:
                            key = True
                            break
                    if not key:
                        break
                    j = k
                    length += 1
                    if length > max_len:
                        max_len = length
        return max_len



if __name__ == '__main__':
    sol = Solution()
    A = [44,46,22,68,45,66,43,9,37,30,50,67,32,47,44,11,15,4,11,6,20,64,54,54,61,63,23,43,3,12,51,61,16,57,14,12,55,17,18,25,19,28,45,56,29,39,52,8,1,21,17,21,23,70,51,61,21,52,25,28]
    # A = [9,4,7,2,10]
    # expect 6
    print(sol.longestArithSeqLength(A))