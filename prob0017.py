"""
电话号码的字母组合
medium

给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
数字到字母的映射，是电话号码按键

输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
"""
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        类似回溯
        """
        if not digits:
            return []
        table = {
            '2': list('abc'),
            '3': list('def'),
            '4': list('ghi'),
            '5': list('jkl'),
            '6': list('mno'),
            '7': list('pqrs'),
            '8': list('tuv'),
            '9': list('wxyz')
        }
        output = []

        def backtrack(combination, next_digits):
            # if there is no more digits to check
            if len(next_digits) == 0:
                # the combination is done
                output.append(combination)
            # if there are still digits to check
            else:
                # iterate over all letters which map
                # the next available digit
                for letter in table[next_digits[0]]:
                    # append the current letter to the combination
                    # and proceed to the next digits
                    backtrack(combination + letter, next_digits[1:])
        backtrack('', digits)
        return output



