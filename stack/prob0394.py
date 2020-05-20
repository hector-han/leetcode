"""
字符串解码
medium

给定一个经过编码的字符串，返回它解码后的字符串。
编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。
你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。
此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。

s = "3[a]2[bc]", 返回 "aaabcbc".
s = "3[a2[c]]", 返回 "accaccacc".
s = "2[abc]3[cd]ef", 返回 "abcabccdcdcdef".

"""


class Solution:
    def decodeString(self, s: str) -> str:
        """
        括号匹配问题，使用stack一层一层解码
        """
        stack = []
        for c in s:
            if c == ']':
                char_seq = []
                k_seq = []
                while stack[-1] != '[':
                    char_seq.append(stack.pop())
                stack.pop()
                while stack and stack[-1] in '0123456789':
                    k_seq.append(stack.pop())
                char_seq.reverse()
                char_str = ''.join(char_seq)
                k_seq.reverse()
                k = int(''.join(k_seq))
                stack.extend(char_str * k)
            else:
                stack.append(c)
        return ''.join(stack)


if __name__ == '__main__':
    sol = Solution()
    s = '2[abc]3[cd]ef'
    print(sol.decodeString(s))

