"""
每日温度
medium

根据每日 气温 列表，请重新生成一个列表，对应位置的输出是需要再等待多久温度才会升高超过该日的天数。如果之后都不会升高，请在该位置用 0 来代替。
例如，给定一个列表 temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，你的输出应该是 [1, 1, 4, 2, 1, 1, 0, 0]。
提示：气温 列表长度的范围是 [1, 30000]。每个气温的值的均为华氏度，都是在 [30, 100] 范围内的整数。

"""
from typing import List


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        """
        从后往前走，如果一直变大，说明后面没有超过的，直接填0。找到局部最大值。之后找到前面第一个大于局部最大值的值，重复此过程
        :param T:
        :return:
        """
        length = len(T)
        if length == 1:
            return [0]
        ans = [0] * length
        j = length - 1
        while j >= 1:
            if T[j-1] >= T[j]:
                j -= 1
            else:
                i = j - 1
                while i >= 0:
                    i -= 1
                cache_i = i


                j = cache_i
        return ans


class Solution2:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        """
        上面的方法虽然逻辑没问题，但复杂度太高了，python过不了。使用单调栈
        思路，如果原始序列是有序递增的，那么栈是满的，单调递减。
        :param T:
        :return:
        """
        length = len(T)
        stack = []
        ans = [0] * length
        for i in range(length-1, -1, -1):
            # 把stack里小于当前的都弹出
            while stack and T[stack[-1]] <= T[i]:
                stack.pop()
            if stack:
                ans[i] = stack[-1] - i
            stack.append(i)
        return ans




if __name__ == '__main__':
    sol = Solution2()
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    print(sol.dailyTemperatures(temperatures))

