"""
在 D 天内送达包裹的能力
medium

传送带上的包裹必须在 D 天内从一个港口运送到另一个港口。
传送带上的第 i 个包裹的重量为 weights[i]。每一天，我们都会按给出重量的顺序往传送带上装载包裹。我们装载的重量不会超过船的最大运载重量。
返回能在 D 天内将传送带上的所有包裹送达的船的最低运载能力。

输入：weights = [1,2,3,4,5,6,7,8,9,10], D = 5
输出：15
解释：
船舶最低载重 15 就能够在 5 天内送达所有包裹，如下所示：
第 1 天：1, 2, 3, 4, 5
第 2 天：6, 7
第 3 天：8
第 4 天：9
第 5 天：10

"""
from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        n = len(weights)

        tmp = 0
        # 计算累计和，后面计算多少天用到
        accu_sum = []
        accu_sum.append(tmp)

        for w in weights:
            tmp += w
            accu_sum.append(tmp)

        def capable(k):
            num_days = 1
            threshold = k
            for i in range(n + 1):
                if accu_sum[i] > threshold:
                    num_days += 1
                    threshold = accu_sum[i - 1] + k
            return num_days <= D

        left, right = max(weights), sum(weights) + 1
        while left < right:
            mid = (left + right) // 2
            if capable(mid):
                right = mid
            else:
                left = mid + 1
        return left


if __name__ == '__main__':
    sol = Solution()
    weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    D = 5
    print(sol.shipWithinDays(weights, D))



