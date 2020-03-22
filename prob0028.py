"""
strStr()
easy
实现子串查找，KMP
kmp substring find algorithm
"""


class Solution:
    def strStr(self, s: str, t: str) -> int:
        m = len(s)
        n = len(t)
        if n == 0:
            return 0

        next_table = [-1] * n
        j, k = 0, -1
        while j < n - 1:
            if k == -1 or t[k] == t[j]:
                k += 1
                j += 1
                next_table[j] = k
            else:
                k = next_table[k]

        i , j = 0, 0
        while i < m:
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j = next_table[j]
                if j == -1:
                    i += 1
                    j += 1
            if j == n:
                return i - n
        return -1


if __name__ == '__main__':
    s = 'aaaaab'
    t = 'aab'
    sol = Solution()
    print(sol.strStr(s, t))

