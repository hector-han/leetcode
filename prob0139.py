"""
给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。
"""
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        worSet = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(n):
            for j in range(i + 1, n + 1):
                if (dp[i] and (s[i:j] in worSet)):
                    dp[j] = True
        return dp[-1]


if __name__ == '__main__':
    sol = Solution()
    s = "leetcode"
    wordDict = ["leet", "code"]
    print(sol.wordBreak(s, wordDict))
    s = "applepenapple"
    wordDict = ["apple", "pen"]
    print(sol.wordBreak(s, wordDict))
    s = "catsandog"
    wordDict = ["cats", "dog", "sand", "and", "cat"]
    print(sol.wordBreak(s, wordDict))