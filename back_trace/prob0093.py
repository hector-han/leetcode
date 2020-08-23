"""
复原IP地址
给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。
有效的 IP 地址正好由四个整数（每个整数位于 0 到 255 之间组成），整数之间用 '.' 分隔。

输入: "25525511135"
输出: ["255.255.11.135", "255.255.111.35"]
"""

from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []

        n = len(s)
        if n <= 3:
            return ans
        def valid(str_num):
            if len(str_num) > 1 and str_num[0] == '0':
                return False
            return 0 <= int(str_num) < 256

        def back_trace(choosed):
            if len(choosed) == 3:
                last = s[choosed[-1]:]
                if valid(last):
                    ips = [s[0:choosed[0]], s[choosed[0]:choosed[1]], s[choosed[1]:choosed[2]], last]
                    ans.append('.'.join(ips))
                return

            last_idx = 0
            if len(choosed) > 0:
                last_idx = choosed[-1]

            for idx in range(last_idx + 1, n):
                tmp = s[last_idx: idx]
                if valid(tmp):
                    choosed.append(idx)
                    back_trace(choosed)
                    choosed.pop()
        back_trace([])
        return ans


if __name__ == '__main__':
    sol = Solution()
    s = '0000'
    print(sol.restoreIpAddresses(s))