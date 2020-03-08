"""
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.
The same repeated number may be chosen from candidates unlimited number of times.

Note:
    All numbers (including target) will be positive integers.
    The solution set must not contain duplicate combinations.
"""

from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        列表元素个数为level=1-target
        cache 是一个dict, cache[val]表示和=val, 且元素个数=level的所有可能的组合
        :param candidates:
        :param target:
        :return:
        """
        length = len(candidates)
        if length == 0:
            return [[]]
        candidates = sorted(candidates)

        cache = {}
        result = []
        for i, val in enumerate(candidates):
            if val > target:
                length = i + 1
                break
            elif val == target:
                result.append([val])
            else:
                cache[val] = [[i]]
        for level in range(2, target + 1):
            cache_new = {}
            for val, indies_list in cache.items():
                for indies in indies_list:
                    for j in range(indies[-1], length):
                        new_val = val + candidates[j]
                        if new_val > target:
                            break
                        elif new_val == target:
                            result.append([candidates[idx] for idx in (indies + [j])])
                        else:
                            if new_val not in cache_new:
                                cache_new[new_val] = []
                            cache_new[new_val].append(indies + [j])
            cache = cache_new
        return result


def is_same(real, expect):
    real_set = [set(ele) for ele in real]
    expect_set = [set(ele) for ele in expect]
    for ele in real_set:
        if ele not in expect_set:
            return False
    for ele in expect_set:
        if ele not in real_set:
            return False
    return True


if __name__ == '__main__':
    candidates = [2, 3, 6, 7]
    target = 7
    result = Solution().combinationSum(candidates, target)
    print(result)
    expect = [
        [7],
        [2,2,3]
    ]
    assert is_same(result, expect)

    candidates = [2,3,5]
    target = 8
    result = Solution().combinationSum(candidates, target)
    print(result)
    expect = [
        [2,2,2,2],
        [2,3,3],
        [3,5]
    ]
    assert is_same(result, expect)






