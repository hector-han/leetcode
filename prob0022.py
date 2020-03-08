"""
Generate Parentheses

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
For example, given n = 3, a solution set is:
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""

from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        every_result = {}
        every_result[0] = []
        every_result[1] = ['()']
        for step in range(2, n+1):
            """"
            get every less than n
            """
            every_result[step] = []
            for loc in range(1, 2*step, 2):
                """
                must be (,_,_,_,...
                the ) match the first can occur in loc 1,3,5,...2*step-1. ie the loc var
                """
                num_1 = (loc - 1) // 2
                if num_1 == 0:
                    piece_1 = ['()']
                else:
                    piece_1 = ['(' + v + ')' for v in every_result[num_1]]

                num_2 = step - num_1 - 1
                if num_2 == 0:
                    every_result[step].extend(piece_1)
                else:
                    tmp = [p1 + p2 for p1 in piece_1 for p2 in every_result[num_2]]
                    every_result[step].extend(tmp)
        return every_result[n]


if __name__ == '__main__':
    solution = Solution()
    solution.generateParenthesis(3)