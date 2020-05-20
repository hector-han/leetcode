"""
戳气球
hard

有 n 个气球，编号为0 到 n-1，每个气球上都标有一个数字，这些数字存在数组 nums 中。
现在要求你戳破所有的气球。每当你戳破一个气球 i 时，你可以获得 nums[left] * nums[i] * nums[right] 个硬币。 这里的 left 和 right 代表和 i 相邻的两个气球的序号。注意当你戳破了气球 i 后，气球 left 和气球 right 就变成了相邻的气球。
求所能获得硬币的最大数量。

输入: [3,1,5,8]
输出: 167
解释: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
     coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167

"""
from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        """
        递归+缓存
        """

        cache = {}
        def _max_coins(tuple_data):
            if tuple_data in cache:
                return cache[tuple_data]
            if len(tuple_data) == 0:
                return 0
            if len(tuple_data) == 1:
                cache[tuple_data] = tuple_data[0]
                return tuple_data[0]
            ans = []
            list_data = list(tuple_data)
            for i in range(len(list_data)):
                first = list_data[i]
                if i == 0:
                    first = first * list_data[1]
                elif i == len(list_data) - 1:
                    first = list_data[-2] * first
                else:
                    first = first * list_data[i-1] * list_data[i+1]
                tmp = first + _max_coins(tuple(list_data[0:i] + list_data[i+1:]))
                ans.append(tmp)
            cache[tuple_data] = max(ans)
            return cache[tuple_data]
        return _max_coins(tuple(nums))


class Solution2:
    def maxCoins(self, nums: List[int]) -> int:
        """
        动态规划， dp[i][j] 戳破[i,j]之间的气球，获得的最大收益
        """
        length = len(nums)
        if length == 0:
            return 0
        pad_nums = [1] + nums + [1]
        length += 2
        dp = [[0] * length for i in range(length)]
        for k in range(2, length):
            for i in range(0, length - k):
                # dp[0][i+k], 迭代最后一个删掉的位置
                dp[i][i+k] = max([dp[i][s] + dp[s][i+k] + pad_nums[s]*pad_nums[i]*pad_nums[i+k] for s in range(i+1, i+k)])
        for v in dp:
            print(v)
        return dp[0][length-1]


if __name__ == '__main__':
    nums = [3,1,5,8]
    sol = Solution()
    print(sol.maxCoins(nums))