"""
Given an array of strings, group anagrams together.
"""

from typing import List


class Solution:
    def getFingerPrint(self, item: str) -> dict:
        ret = [0] * 26
        for c in item:
            idx = ord(c) - ord('a')
            ret[idx] += 1
        return ret

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        tmp = {}
        for ele in strs:
            _fg = tuple(self.getFingerPrint(ele))
            if _fg not in tmp:
                tmp[_fg] = []
            tmp[_fg].append(ele)
        ret = []
        for val in tmp.values():
            ret.append(val)
        return ret


if __name__ == '__main__':
    sol = Solution()
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    ans = sol.groupAnagrams(strs)
    print(ans)



