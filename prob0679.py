"""
hard
24点游戏

你有 4 张写有 1 到 9 数字的牌。你需要判断是否能通过 *，/，+，-，(，) 的运算得到 24。
输入: [4, 1, 8, 7]
输出: True
解释: (8-4) * (7-1) = 24
"""
from typing import List


class Solution:

    def compute(self, a, b):
        """
        计算 a, b所有可能的结果
        """
        ans = []
        ans.append(a+b)
        ans.append(a-b)
        ans.append(b-a)
        ans.append(a*b)
        if b != 0:
            ans.append(a / b)
        if a != 0:
            ans.append(b / a)
        return set(ans)

    def compute2set(self, seta, setb):
        ans = set()
        for a in seta:
            for b in setb:
                for t in self.compute(a, b):
                    ans.add(t)
        return ans

    def valid(self, path):
        """
        某一种全排列，是否可以算出24
        """
        # 1,3
        ans12 = self.compute(path[1], path[2])
        ans123 = self.compute2set(ans12, [path[3]])
        ans01234 = self.compute2set([path[0]], ans123)
        for t in ans01234:
            if abs(t-24) < 1e-3:
                return True

        ans01 = self.compute(path[0], path[1])
        ans23 = self.compute(path[2], path[3])
        ans0123 = self.compute2set(ans01, ans23)
        for t in ans0123:
            if abs(t-24) < 1e-3:
                return True
        return False

    def judgePoint24(self, nums: List[int]) -> bool:
        """
        找到所有全排列，全排列内部是从前往后计算
        对于找到的每一个全排列，分成1,3和2,2两种。对于+,*两个，直接计算即可。对于/ -, 前后两种都计算下
        有冗余就有冗余吧
        """
        self.ans = False

        def back_trace(path: list):

            if len(path) == 4:
                # 已经选取了一种全排列
                if self.valid([nums[i] for i in path]):
                    self.ans = True
                return

            if self.ans:
                return True

            for i in range(4):
                if i in path:
                    continue
                path.append(i)
                back_trace(path)
                path.pop()
        back_trace([])
        return self.ans


if __name__ == '__main__':
    nums = [4,1,8,7]
    nums = [1,2,1,2]
    sol = Solution()
    print(sol.judgePoint24(nums))




