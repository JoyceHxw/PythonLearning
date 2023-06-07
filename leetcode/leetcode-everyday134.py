# 有两只老鼠和 n 块不同类型的奶酪，每块奶酪都只能被其中一只老鼠吃掉。
# 下标为 i 处的奶酪被吃掉的得分为：
# 如果第一只老鼠吃掉，则得分为 reward1[i] 。
# 如果第二只老鼠吃掉，则得分为 reward2[i] 。
# 给你一个正整数数组 reward1 ，一个正整数数组 reward2 ，和一个非负整数 k 。
# 请你返回第一只老鼠恰好吃掉 k 块奶酪的情况下，最大 得分为多少。


class Solution:
    def miceAndCheese(self, reward1: list[int], reward2: list[int], k: int) -> int:
        # 运用和，只需要进行一次排序
        ans = 0
        n = len(reward1)
        diffs = [reward1[i] - reward2[i] for i in range(n)]
        ans += sum(reward2)
        diffs.sort()
        for i in range(1, k+1):
            ans += diffs[n - i]
        return ans

S=Solution()
print(S.miceAndCheese([4,1,5,3,3],[3,4,1,5,2],3))