

class Solution:
    def isMathRecursive(self, i, j) -> bool:
        """
        p =  a b* c.
        s = a b b c
        substring s[i:] match subpattern p[j:] or not.
        :param i: i is the subscription of string to be match.
        :param j: j is the subscription of pattern. ie. j=0 means the location before a,
            j=2 means the location before c. b* is an arch so treated as one single ele.
        :return: bool
        """
        # string and pattern both reach the last exactly, return true
        if i == self.s_len and j == self.p_len:
            return True

        if j == self.p_len:
            return False

        if j + 1 < self.p_len and self.p[j+1] == '*':
            next_j = j + 2
        else:
            next_j = j + 1

        if i == self.s_len:
            if next_j == j + 1:
                return False
            else:
                return self.isMathRecursive(i, next_j)

        # pattern is x*, j need to increase 2 or stay same
        if next_j == j+2:
            if self.p[j] == '.' or self.p[j] == self.s[i]:
                return self.isMathRecursive(i+1, next_j) or self.isMathRecursive(i, next_j) or self.isMathRecursive(i+1, j)
            else:
                return self.isMathRecursive(i, next_j)
        else:
            # next char of pattern is not *, just match
            if self.p[j] == '.' or self.p[j] == self.s[i]:
                return self.isMathRecursive(i+1, next_j)
            else:
                return False

    def simplify_pattern(self, p: str) -> str:
        """
        reduce pattern a*a*a*a*bcd to a*bcd
        :param p: pattern
        :return: reduced pattern
        """
        ret = []
        max_len = len(p)
        met_star = False
        _star = '*'
        i = 0
        while i < max_len:
            if met_star:
                if i + 1 < max_len and p[i+1] == '*' and p[i] == _star:
                    i += 2
                else:
                    ret.append(p[i])
                    met_star = False
                    _star = '*'
                    i += 1
            else:
                ret.append(p[i])
                if p[i] == '*':
                    met_star = True
                    _star = p[i-1]
                i += 1

        return ''.join(ret)

    def isMatch(self, s: str, p: str) -> bool:
        self.s = s
        self.p = self.simplify_pattern(p)
        self.s_len = len(self.s)
        self.p_len = len(self.p)
        return self.isMathRecursive(0, 0)


if __name__ == '__main__':
    test_cases = [
        ('aa', 'a', False),
        ('aa', 'a*', True),
        ('ab', '.*', True),
        ('aab', 'c*a*b', True),
        ('mississippi', 'mis*is*p*.', False),
        ('a', 'ab*', True),
        ('ab', '.*c', False),
        ('aaaaaaaaaaaaab', 'a*a*a*a*a*a*a*a*a*a*c', False)
    ]

    for s, p, ret in test_cases:
        solution = Solution()
        print(solution.isMatch(s, p), ret)


