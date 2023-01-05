# 给你一个整数数组 nums （下标 从 0 开始 计数）以及两个整数：low 和 high ，请返回 漂亮数对 的数目。
# 漂亮数对 是一个形如 (i, j) 的数对，其中 0 <= i < j < nums.length 且 low <= (nums[i] XOR nums[j]) <= high 。

# 暴力拆解超过时间限制
# class Solution:
#     def countPairs(self, nums: list[int], low: int, high: int) -> int:
#         cnt=0
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
#                 if low<=(nums[i] ^ nums[j])<=high:
#                     cnt+=1
#         return cnt


# 字典树
# https://leetcode.cn/problems/count-pairs-with-xor-in-a-range/solution/tong-ji-yi-huo-zhi-zai-fan-wei-nei-de-sh-cu18/
HIGH_BIT = 14

class TrieNode:
    def __init__(self):
        self.children = [None, None]
        self.sum = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, num: int) -> None:
        cur = self.root
        for k in range(HIGH_BIT, -1, -1):
            bit = (num >> k) & 1
            if not cur.children[bit]:
                cur.children[bit] = TrieNode()
            cur = cur.children[bit]
            cur.sum += 1

    def get(self, num: int, x: int) -> int:
        res = 0
        cur = self.root
        for k in range(HIGH_BIT, -1, -1):
            bit = (num >> k) & 1
            if (x >> k) & 1:
                if cur.children[bit]:
                    res += cur.children[bit].sum
                if not cur.children[bit ^ 1]:
                    return res
                cur = cur.children[bit ^ 1]
            else:
                if not cur.children[bit]:
                    return res
                cur = cur.children[bit]
        res += cur.sum
        return res

class Solution:
    def countPairs(self, nums: list[int], low: int, high: int) -> int:
        def f(nums: list[int], x: int) -> int:
            res = 0
            trie = Trie()
            for i in range(1, len(nums)):
                trie.add(nums[i - 1])
                res += trie.get(nums[i], x)
            return res
        return f(nums, high) - f(nums, low - 1)

