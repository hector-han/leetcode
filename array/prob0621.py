"""
任务调度器
medium

给定一个用字符数组表示的 CPU 需要执行的任务列表。其中包含使用大写的 A - Z 字母表示的26 种不同种类的任务。任务可以以任意顺序执行，并且每个任务都可以在 1 个单位时间内执行完。CPU 在任何一个单位时间内都可以执行一个任务，或者在待命状态。
然而，两个相同种类的任务之间必须有长度为 n 的冷却时间，因此至少有连续 n 个单位时间内 CPU 在执行不同的任务，或者在待命状态。
你需要计算完成所有任务所需要的最短时间。

输入：tasks = ["A","A","A","B","B","B"], n = 2
输出：8
解释：A -> B -> (待命) -> A -> B -> (待命) -> A -> B.

"""
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        先读到一个map里，然后排序，按从多到少一个一个安排。如果第一个可以安排，那后续顺序即可。否则添加待命
        """
        if len(tasks) == 0:
            return 0
        task_cnt = {}
        for t in tasks:
            if not t in task_cnt:
                task_cnt[t] = 0
            task_cnt[t] += 1
        num_task = len(task_cnt)
        sorted_cnt = sorted(task_cnt.items(), key=lambda x: x[1], reverse=True)
        ans = 0
        last_max_id = - n - 2
        while sorted_cnt[0][1] > 0:
            i = 0
            while i < n + 1:
                if task_cnt[sorted_cnt[0][0]] == 0:
                    break
                if i < num_task and sorted_cnt[i][1] > 0:
                    task_cnt[sorted_cnt[i][0]] -= 1
                ans += 1
                i += 1
            sorted_cnt = sorted(task_cnt.items(), key=lambda x: x[1], reverse=True)

        return ans


if __name__ == '__main__':
    tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"]
    # tasks = ["A","A","A","B","B","B"]
    sol = Solution()
    print(sol.leastInterval(tasks, 2))

