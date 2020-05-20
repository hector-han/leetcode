"""
前 K 个高频元素
medium
给定一个非空的整数数组，返回其中出现频率前 k 高的元素。
"""
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_count = {}
        for n in nums:
            if n not in dict_count:
                dict_count[n] = 0
            dict_count[n] += 1
        sorted_count = sorted(dict_count.items(), key=lambda x: x[1], reverse=True)
        return [v[0] for v in sorted_count[0:k]]

