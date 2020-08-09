"""
medium

给定两个整数，分别表示分数的分子 numerator 和分母 denominator，以字符串形式返回小数。

如果小数部分为循环小数，则将循环的部分括在括号内。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/fraction-to-recurring-decimal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        neg = False
        if numerator < 0:
            numerator = -numerator
            neg = not neg
        if denominator < 0:
            denominator = -denominator
            neg = not neg

        dev = numerator // denominator
        remain = numerator % denominator

        prefix = ''
        if neg:
            prefix = '-'
        if remain == 0:
            if dev == 0:
                return str(dev)
            return prefix + str(dev)

        ds = []
        rs = []
        loop_pointer = -1
        while remain != 0:
            rs.append(remain)
            tmp = 10 * remain
            d = tmp // denominator
            remain = tmp % denominator
            ds.append(d)
            for i, v in enumerate(rs):
                if v == remain:
                    loop_pointer = i
                    break
            if loop_pointer != -1:
                break

        ds = [str(v) for v in ds]
        if loop_pointer == -1:
            return prefix + '{}.{}'.format(str(dev), ''.join(ds))
        else:
            part_1 = ''.join(ds[0:loop_pointer])
            part_2 = '(' + ''.join(ds[loop_pointer:]) + ')'
            return prefix + '{}.{}{}'.format(str(dev), part_1, part_2)


if __name__ == '__main__':
    sol = Solution()
    print(sol.fractionToDecimal(2, 1))
    print(sol.fractionToDecimal(1, 2))
    print(sol.fractionToDecimal(2, 3))