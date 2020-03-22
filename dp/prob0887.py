"""
高楼扔鸡蛋

hard

你将获得 K 个鸡蛋，并可以使用一栋从 1 到 N  共有 N 层楼的建筑。
每个蛋的功能都是一样的，如果一个蛋碎了，你就不能再把它掉下去。
你知道存在楼层 F ，满足 0 <= F <= N 任何从高于 F 的楼层落下的鸡蛋都会碎，从 F 楼层或比它低的楼层落下的鸡蛋都不会破。
每次移动，你可以取一个鸡蛋（如果你有完整的鸡蛋）并把它从任一楼层 X 扔下（满足 1 <= X <= N）。
你的目标是确切地知道 F 的值是多少。
无论 F 的初始值如何，你确定 F 的值的最小移动次数是多少？

输入：K = 1, N = 2
输出：2
解释：
鸡蛋从 1 楼掉落。如果它碎了，我们肯定知道 F = 0 。
否则，鸡蛋从 2 楼掉落。如果它碎了，我们肯定知道 F = 1 。
如果它没碎，那么我们肯定知道 F = 2 。
因此，在最坏的情况下我们需要移动 2 次以确定 F 是多少。
"""
import time


class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        """
        会ETL
        """
        s = time.time()
        dp_table = []
        for i in range(K):
            dp_table.append([0] * (N+1))
        for j in range(N+1):
            dp_table[0][j] = j

        for i in range(1, K):
            for j in range(1, N+1):
                res = j
                for k in range(1, j+1):
                    # k层碎了，i-1个鸡蛋，k-1楼层
                    f1 = dp_table[i-1][k-1]
                    # k层没碎，i个鸡蛋，j-k楼层
                    f2 = dp_table[i][j-k]
                    m = max(f1, f2) + 1
                    if m < res:
                        res = m
                dp_table[i][j] = res
        e=time.time()
        print('time elapse:{}', e-s)
        return dp_table[K-1][N]





class Solution2:
    def superEggDrop(self, K: int, N: int) -> int:
        """
        会ETL
        """
        s = time.time()

        # 先获得无限鸡蛋的理论最小值
        theo_list = [0] * (N+1)
        for i in range(1, N+1):
            mid = (1 + i) // 2
            left_num = mid - 1
            right_num = i - mid
            theo_list[i] = max(theo_list[left_num], theo_list[right_num]) + 1
        if K >= theo_list[N]:
            return theo_list[N]

        dp_table = []
        for i in range(K):
            dp_table.append([0] * (N+1))
        for j in range(N+1):
            dp_table[0][j] = j

        for i in range(1, K):
            for j in range(1, N+1):
                if i >= theo_list[j]:
                    dp_table[i][j] = theo_list[j]
                    continue
                res = j
                # for k in range(1, j+1):
                # f1 = dp_table[i-1][k-1]
                # f2 = dp_table[i][j-k]
                # f1 关于k递增，f2关于k递减
                low = 1
                high = j
                while low <= high:
                    k = (low + high) // 2
                    f1 = dp_table[i - 1][k - 1]
                    f2 = dp_table[i][j - k]
                    m = max(f1, f2) + 1
                    if m < res:
                        res = m
                    if f1 < f2:
                        low = k + 1
                    else:
                        high = k - 1

                dp_table[i][j] = res
        e=time.time()
        print('time elapse:{}', e-s)
        return dp_table[K-1][N]


class Solution3:
    def superEggDrop(self, K: int, N: int) -> int:
        """
        dp_table[k][m] k个鸡蛋，扔m次，在最坏情况下可以确定的最高楼层数
        逆向思维
        dp[k][m] = dp[k][m-1] + dp[k-1][m-1] + 1
        只用两个即可
        """
        dp_table = []
        for k in range(K):
            # k+1 个鸡蛋
            dp_table.append([0] * N)

        for j in range(N):
            # 1个鸡蛋扔j+1次，确定j+1楼
            dp_table[0][j] = j+1
        for k in range(K):
            # 不管几个鸡蛋，扔1次最多只能确定1楼
            dp_table[k][0] = 1


        m = 0
        while dp_table[K-1][m] < N:
            m += 1
            for k in range(1, K):
                dp_table[k][m] = dp_table[k][m-1] + dp_table[k-1][m-1] + 1
        return m + 1


if __name__ == '__main__':
    sol = Solution3()
    print(sol.superEggDrop(1,2)) # 2
    print(sol.superEggDrop(2, 6)) # 3
    print(sol.superEggDrop(3, 14)) #4
    print(sol.superEggDrop(4, 5000))  # 19
    print(sol.superEggDrop(13, 8191))  # 13


