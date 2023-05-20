# 给你一棵以 root 为根的 二叉树 ，请你返回 任意 二叉搜索子树的最大键值和。
# 二叉搜索树的定义如下：
# 任意节点的左子树中的键值都 小于 此节点的键值。
# 任意节点的右子树中的键值都 大于 此节点的键值。
# 任意节点的左子树和右子树都是二叉搜索树


# Definition for a binary tree node.
from cmath import inf
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxSumBST(self, root: TreeNode) -> int:
        ans=0
        # 递归函数返回一个元组：
        # 以该节点为根的数是否是搜索树，节点中最小值，节点中最大值，所有节点之和
        def dfs(root):
            if root is None:
                return 1, inf, -inf, 0
            l_bst, l_min, l_max, l_s=dfs(root.left)
            r_bst, r_min, r_max, r_s=dfs(root.right)
            if l_bst and r_bst and root.val>l_max and root.val<r_min:
                nonlocal ans
                s = l_s + r_s + root.val
                ans = max(ans, s)
                return 1, min(l_min, root.val), max(r_max, root.val), s
            return 0,0,0,0

        dfs(root)
        return ans