"""
比特位计数
medium

给定一个非负整数 num。对于 0 ≤ i ≤ num 范围中的每个数字 i ，计算其二进制数中的 1 的数目并将它们作为数组返回。
输入: 2
输出: [0,1,1]

"""
from typing import List


class Solution:
    def countBits(self, num: int) -> List[int]:
        dp = [0] * (num + 1)
        dp[0] = 0
        # 奇数=偶数+1,偶数=/2的数
        i = 1
        while i < num + 1:
            if i % 2 == 1:
                dp[i] = dp[i-1] + 1
            else:
                dp[i] = dp[i // 2]
            i += 1
        return dp

