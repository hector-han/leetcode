"""
给定 S 和 T 两个字符串，当它们分别被输入到空白的文本编辑器后，判断二者是否相等，并返回结果。 # 代表退格字符。
注意：如果对空文本输入退格字符，文本继续为空。

"""

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def _precess(s: str):
            stack = []
            for c in s:
                if c == '#':
                    if stack:
                        stack.pop()
                else:
                    stack.append(c)
            return ''.join(stack)
        return _precess(S) == _precess(T)


if __name__ == '__main__':
    S = 'a##c'
    T = '#a#c'
    sol = Solution()
    print(sol.backspaceCompare(S, T))