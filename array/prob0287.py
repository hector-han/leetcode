"""
寻找重复数
medium

给定一个包含 n + 1 个整数的数组 nums，其数字都在 1 到 n 之间（包括 1 和 n），可知至少存在一个重复的整数。假设只有一个重复的整数，找出这个重复的数。

输入: [1,3,4,2,2]
输出: 2

不能更改原数组（假设数组是只读的）。
只能使用额外的 O(1) 的空间。
时间复杂度小于 O(n2) 。
数组中只有一个重复的数字，但它可能不止重复出现一次。
"""
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        nums想象成从id -> nums[id]的映射，或者是单链表
        节点编号0~n,共n+1个。 id->nums[id]连接起来，nums[id]范围在[1,n],必然有环。
        反证，假设没环，最后一个可以认为连接到了0,那么是个大环，也就是说nums是0~n的一个置换，事实上不是。所以必然有环。
        从0出发必然有环，结合快慢指针，即可得到答案。
        """
        slow = 0
        fast = 0
        while slow == 0 or slow != fast:
            slow = nums[slow]
            fast = nums[fast]
            fast = nums[fast]
        # slow = fast, 之后一个一个递进
        fast = 0
        while fast != slow:
            fast = nums[fast]
            slow = nums[slow]
        return slow


if __name__ == '__main__':
    sol = Solution()
    nums = [3,1,3,4,2]
    print(sol.findDuplicate(nums))



