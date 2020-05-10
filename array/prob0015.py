"""
三数之和
medium
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。
注意：答案中不可以包含重复的三元组。

 
示例：
给定数组 nums = [-1, 0, 1, 2, -1, -4]，
满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]

"""
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        cache = {}
        for n in nums:
            if n not in cache:
                cache[n] = 0
            cache[n] += 1

        # 回溯求解
        ans = []
        unique_nums = sorted(cache.keys())
        length = len(unique_nums)
        print(unique_nums)
        def back_tack(path):
            if len(path) == 2:
                # print(cache)
                n0 = unique_nums[path[0]]
                n1 = unique_nums[path[1]]
                need = -(n0 + n1)
                if need >= n1:
                    if need in cache and cache[need] > 0:
                        ans.append([n0, n1, need])
                return
            max_id = 0
            if path:
                max_id = path[-1]
            for i in range(max_id, length):
                path.append(i)
                i_num = unique_nums[i]
                cache[i_num] -= 1
                if cache[i_num] >= 0:
                    back_tack(path)
                path.pop()
                cache[i_num] += 1

        back_tack([])
        return ans



if __name__ == '__main__':
    nums = nums = [-1, 0, 1]
    sol = Solution()
    print(sol.threeSum(nums))