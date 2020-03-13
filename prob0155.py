"""
设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。

    push(x) -- 将元素 x 推入栈中。
    pop() -- 删除栈顶的元素。
    top() -- 获取栈顶元素。
    getMin() -- 检索栈中的最小元素。
"""

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.helper = []


    def push(self, x: int) -> None:
        self.data.append(x)
        if len(self.helper) < 1 or x < self.helper[-1]:
            self.helper.append(x)
        else:
            self.helper.append(self.helper[-1])


    def pop(self) -> None:
        self.helper.pop()
        return self.data.pop()


    def top(self) -> int:
        return self.data[-1]


    def getMin(self) -> int:
        return self.helper[-1]