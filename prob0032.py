"""
Longest Valid Parentheses

Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"

Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"
"""


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        """
        依次入栈，把能消掉的都消掉，最后栈里面的都是不能匹配的
        这些括号的可以看成分界线，他们之间消掉的都是well-formed的括号，统计分界线的距离，找出最大的即可
        """
        length = len(s)
        if length <= 1:
            return 0
        stack = []
        for i in range(0, length):
            if len(stack) == 0:
                stack.append((s[i], i))
                continue
            if stack[-1][0] == '(' and s[i] == ')':
                stack.pop()

            else:
                stack.append((s[i], i))

        barriers = [-1] + [ele[1] for ele in stack] + [length]
        maximum = 0
        length = len(barriers)
        for i in range(length - 1):
            tmp = barriers[i + 1] - barriers[i] - 1
            if tmp > maximum:
                maximum = tmp
        return maximum


if __name__ == '__main__':
    sol = Solution()
    print(sol.longestValidParentheses('(()'))
    print(sol.longestValidParentheses(')()())'))
