class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {
            '}': '{',
            ')': '(',
            ']': '['
        }

        for c in s:
            if c in brackets.keys():
                i = len(stack) - 1
                while i >= 0:
                    if stack[i] == brackets[c]:
                        break
                    elif stack[i] in brackets.values():
                        return False
                    else:
                        i -= 1
                if i < 0:
                    return False
                stack = stack[0:i]
            else:
                stack.append(c)
        for c in stack:
            if c in brackets.values():
                return False
        return True


