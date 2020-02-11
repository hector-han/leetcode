"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.
"""
from typing import List


class Solution:
    def get_vol(self, height, begin, end, h):
        """
        从begin 到 end, 高度为h的水的容量
        """
        vol = 0
        for i in range(begin + 1, end):
            vol += (h - height[i])
        return vol

    def trap(self, height: List[int]) -> int:
        list_len = len(height)
        i = 0
        vol = 0
        while i < list_len:
            left_h = height[i]
            j = i + 1

            if j == list_len:
                return vol

            cache = {}
            while j < list_len:
                right_h = height[j]
                if right_h >= left_h:
                    #找到一个，开始计算容量
                    v_tmp = self.get_vol(height, i, j, left_h)
                    vol += v_tmp
                    break
                else:
                    if right_h not in cache:
                        cache[right_h] = j
                    j += 1
            if j == list_len:
                while left_h > 0:
                    left_h -= 1
                    if left_h in cache:
                        j = cache[left_h]
                        v_tmp = self.get_vol(height, i, j, left_h)
                        vol += v_tmp
                        break
            i = j
        return vol


if __name__ == '__main__':
    sol = Solution()
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    output = sol.trap(height)
    print(output)
    assert output == 6
