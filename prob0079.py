"""
单词搜索
medium

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.
"""
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        k = len(word)
        if k == 0:
            return False

        def back_track(i,j, idx):
            # print(idx, i, j, board)
            if idx == k:
                return True
            if i>=0 and i < m and j>=0 and j < n and board[i][j] == word[idx]:
                board[i][j] = '.'
                if back_track(i-1, j, idx+1):
                    board[i][j] = word[idx]
                    return True
                if back_track(i+1, j, idx+1):
                    board[i][j] = word[idx]
                    return True
                if back_track(i, j-1, idx+1):
                    board[i][j] = word[idx]
                    return True
                if back_track(i, j+1, idx+1):
                    board[i][j] = word[idx]
                    return True
                board[i][j] = word[idx]
            return False

        for i in range(m):
            for j in range(n):
                # print('i,j=', i, j)
                if back_track(i,j,0):
                    return True
        return False


if __name__ == '__main__':
    board =[
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]

    sol = Solution()
    word = "ABCCED"
    print(sol.exist(board, word))
    word = "SEE"
    print(sol.exist(board, word))
    word = "ABCB"
    print(sol.exist(board, word))