"""
找到字符串中所有字母异位词
medium

给定一个字符串 s 和一个非空字符串 p，找到 s 中所有是 p 的字母异位词的子串，返回这些子串的起始索引。
字符串只包含小写英文字母，并且字符串 s 和 p 的长度都不超过 20100。

字母异位词指字母相同，但排列不同的字符串。
不考虑答案输出的顺序。
"""
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """
        滑动窗口
        """
        cache = {}
        sum = 0
        for c in p:
            if c not in cache:
                cache[c] = 0
            cache[c] += 1
            sum += 1
        expected = len(p)
        length = len(s)
        j = 0
        ans = []
        while j < length and j < expected:
            c = s[j]
            if c in cache:
                cache[c] -= 1
            j += 1
        if j != expected:
            return ans
        def _check(cache):
            for k in cache:
                if cache[k] != 0:
                    return False
            return True
        while j < length:
            if _check(cache):
                ans.append(j-expected)
            if s[j] in cache:
                cache[s[j]] -= 1
            if s[j-expected] in cache:
                cache[s[j-expected]] += 1
            j += 1
        if _check(cache):
            ans.append(j - expected)
        return ans

if __name__ == '__main__':
    s='cbaebabacd'
    p='abc'
    sol = Solution()
    print(sol.findAnagrams(s, p))
