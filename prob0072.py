"""
Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.
"""

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        matrix = [[0 for j in range(n+1)] for i in range(m+1)]
        for i in range(1, m+1):
            matrix[i][0] = i
        for j in range(1, n+1):
            matrix[0][j] = j

        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    matrix[i][j] = matrix[i-1][j-1]
                else:
                    tmp = min(matrix[i-1][j-1], matrix[i][j-1], matrix[i-1][j])
                    matrix[i][j] = tmp + 1
        return matrix[m][n]


if __name__ == '__main__':
    sol = Solution()
    word1 = "intention"
    word2 = "execution"
    assert sol.minDistance(word1, word2) == 5

    word1 = "horse"
    word2 = "ros"
    assert sol.minDistance(word1, word2) == 3