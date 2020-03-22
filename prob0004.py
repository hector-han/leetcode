"""
寻找两个有序数组的中位数
hard

给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。
请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
你可以假设 nums1 和 nums2 不会同时为空。

nums1 = [1, 3]
nums2 = [2]
则中位数是 2.0

解题思路比较复杂，直接看题目答案。简要说下思路。
可以假设第一个列表长度m<=第二个列表长度n

a[0]...a[i-1] | a[i]...a[m-1]
b[0]...b[j-1] | b[j]...b[n-1]

找到i,j，让左边和右边元素个数一样（或者左边刚好多1），并且满足a[i-1]<=b[j], b[j-1]<=a[i]

i 从 [0...m]，由 i+j = m-i + n-j or i+j = m-i+n-j+1 可以得出，j=(m+n+1) // 2 - i，两种情况都适用。

那么其实只要检查满足的不等号条件即可。然后如果是边界值，特殊处理下。

"""
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        if m > n:
            nums1, nums2 = nums2, nums1
            m, n = n, m

        i_min, i_max = 0, m
        i, j = 0, 0
        while i_min <= i_max:
            i = (i_min + i_max) // 2
            j = (m+n+1) // 2 - i
            if m == 0:
                break
            if i == 0:
                if nums2[j-1] <= nums1[i]:
                    break
                else:
                    i_min = i + 1
            elif i == m:
                if nums1[i-1] <= nums2[j]:
                    break
                else:
                    i_max = i - 1
            else:
                if nums1[i-1] <= nums2[j] and nums2[j-1] <= nums1[i]:
                    break
                elif nums1[i-1] > nums2[j]:
                    i_max = i - 1
                else:
                    i_min = i + 1
        if i == 0:
            max_of_left = nums2[j - 1]
        elif j == 0:
            max_of_left = nums1[i - 1]
        else:
            max_of_left = max(nums1[i - 1], nums2[j - 1])

        if (m + n) % 2 == 1:
            return max_of_left

        if i == m:
            min_of_right = nums2[j]
        elif j == n:
            min_of_right = nums1[i]
        else:
            min_of_right = min(nums1[i], nums2[j])

        return (max_of_left + min_of_right) / 2.0




if __name__ == '__main__':
    nums1 = []
    nums2 = [1]
    sol = Solution()
    print(sol.findMedianSortedArrays(nums1, nums2))






