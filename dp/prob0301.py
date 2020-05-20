"""
删除无效的括号
hard

删除最小数量的无效括号，使得输入的字符串有效，返回所有可能的结果。
说明: 输入可能包含了除 ( 和 ) 以外的字符。

太难了，放弃吧

输入: "(a)())()"
输出: ["(a)()()", "(a())()"]
"""
from typing import List


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        if not s:
            return [s]
        length = len(s)
        i = 0
        j = length - 1
        while i < length and s[i] != '(':
            i += 1
        while j >= 0 and s[j] != ')':
            j -= 1
        if j < i:
            return [s.replace(')', '').replace('(', '')]
        # must i < j
        prefix = s[0:i]
        suffix = s[j+1:]
        cleaned = s[i:j+1]
        length2 = len(cleaned)
        no = 0
        no_list = [0] * length2
        for i in range(length2):
            if cleaned[i] == '(':
                no += 1
                no_list[i] = no
            elif cleaned[i] == ')':
                no -= 1
                no_list[i] = no
        