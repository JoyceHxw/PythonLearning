# 给你一个整数数组 arr，请你将该数组分隔为长度 最多 为 k 的一些（连续）子数组。分隔完成后，每个子数组的中的所有值都会变为该子数组中的最大值。
# 返回将数组分隔变换后能够得到的元素最大和。本题所用到的测试用例会确保答案是一个 32 位整数。

class Solution:
    def maxSumAfterPartitioning(self, arr: list[int], k: int) -> int:
        # 动态规划
        n = len(arr)
        f = [0] * (n + 1) # 基于第i-k到第i-1个的最大值来计算第i个
        for i in range(1, n + 1):  # 前i个数
            mx = 0
            # 从后向前遍历，更新最大值mx，从1到k计算最大值
            for j in range(i, max(0, i - k), -1):  # 前i个数的后k个数
                mx = max(mx, arr[j - 1]) # 维护最大值
                f[i] = max(f[i], f[j - 1] + mx * (i - j + 1))  # 维护前i个数的最大和
                # print(f)
        return f[n]
