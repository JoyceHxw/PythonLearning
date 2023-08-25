# 给你一棵根为 root 的二叉树，请你返回二叉树中好节点的数目。
# 「好节点」X 定义为：从根到该节点 X 所经过的节点中，没有任何节点的值大于 X 的值。

from cmath import inf

# 直观的dfs
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # 记录每条路径上的最大值，进行比较
        ans=0
        max_num=-inf
        def dfs(root,max_num):
            if root==None:
                return
            if root.val>=max_num:
                nonlocal ans
                ans+=1
                max_num=root.val
            dfs(root.left,max_num)
            dfs(root.right,max_num)
        dfs(root,max_num)
        return ans