# 在一个无限的 x 坐标轴上，有许多水果分布在其中某些位置。给你一个二维整数数组 fruits ，其中 fruits[i] = [positioni, amounti] 表示共有 amounti 个水果放置在 positioni 上。fruits 已经按 positioni 升序排列 ，每个 positioni 互不相同 。
# 另给你两个整数 startPos 和 k 。最初，你位于 startPos 。从任何位置，你可以选择 向左或者向右 走。在 x 轴上每移动 一个单位 ，就记作 一步 。你总共可以走 最多 k 步。你每达到一个位置，都会摘掉全部的水果，水果也将从该位置消失（不会再生）。
# 返回你可以摘到水果的 最大总数 。

class Solution:
    def maxTotalFruits(self, fruits: list[list[int]], startPos: int, k: int) -> int:
        # 双指针，考虑所有可能区间
        ans = i = s = 0
        # 注意区间的边界，不用考虑没有水果的位置
        for j, (pj, fj) in enumerate(fruits):
            s += fj
            # 覆盖区间的步数
            while i <= j and pj - fruits[i][0] + min(abs(startPos - fruits[i][0]), abs(startPos - fruits[j][0])) > k:
                s -= fruits[i][1]  # 该位置上必然有水果，只考虑了有水果的区间
                i += 1
            ans = max(ans, s)
        return ans