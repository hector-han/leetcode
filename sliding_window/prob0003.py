"""
无重复字符的最长子串
medium

给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:
输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        window_count = {}
        left = 0
        right = 0
        ans = 0
        while right < n:
            if s[right] not in window_count:
                window_count[s[right]] = 1
                right += 1
            elif window_count[s[right]] == 0:
                window_count[s[right]] += 1
                right += 1
            else:
                ans = max(ans, right - left)
                while window_count[s[right]] > 0:
                    window_count[s[left]] -= 1
                    left += 1
        ans = max(ans, n-left)
        return ans


if __name__ == '__main__':
    s = "abcabcbb"
    sol = Solution()
    print(sol.lengthOfLongestSubstring(s))

