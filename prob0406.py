"""
根据身高重建队列
medium
假设有打乱顺序的一群人站成一个队列。 每个人由一个整数对(h, k)表示，其中h是这个人的身高，k是排在这个人前面且身高大于或等于h的人数。 编写一个算法来重建这个队列。

输入:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

输出:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]

"""
from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        high_to_low = sorted(people, key=lambda x: (-x[0], x[1]))
        ans = []
        for i, pair in enumerate(high_to_low):
            # 相对位置正确
            if pair[1] == i:
                ans.append(pair)
                continue
            else:
                # 放到正确的位置上
                ans.insert(pair[1], pair)
        return ans



if __name__ == '__main__':
    people = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
    sol = Solution()
    print(sol.reconstructQueue(people))