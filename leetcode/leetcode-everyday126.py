# 给你二叉树的根节点 root 和一个整数 limit ，请你同时删除树中所有 不足节点 ，并返回最终二叉树的根节点。
# 假如通过节点 node 的每种可能的 “根-叶” 路径上值的总和全都小于给定的 limit，则该节点被称之为 不足节点 ，需要被删除。
# 叶子节点，就是没有子节点的节点。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:
        # 根到叶子节点求和
        # 返回是否大于limit
        def dfs(root: TreeNode, s: int, limit:int):
            if root==None:
                return False
            if root.left==None and root.right==None:
                s+=root.val
                if s>=limit:
                    return True
                else:
                    return False
            s+=root.val
            isleft=dfs(root.left,s,limit)
            isright=dfs(root.right,s,limit)
            s-=root.val
            if isleft==False:
                root.left=None
            if isright==False:
                root.right=None
            return isleft or isright
        return root if dfs(root,0,limit) else None