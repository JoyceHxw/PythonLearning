# 给定二叉树的根节点 root，找出存在于 不同 节点 A 和 B 之间的最大值 V，其中 V = |A.val - B.val|，且 A 是 B 的祖先。
# （如果 A 的任何子节点之一为 B，或者 A 的任何子节点是 B 的祖先，那么我们认为 A 是 B 的祖先）

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        # DFS递推：只能遍历，不能保存每条路径上节点的值
        # v=0
        # stack=[]
        # node=root
        # while node!=None or stack!=[]:
        #     while node!=None:
        #         stack.append(node) # 中序遍历
        #         print(node.val)
        #         node=node.left
        #     node=stack[-1].right
        #     stack.pop()
        # return v

        # 适合递归，每一条根节点到叶子节点的路径上的点都有
        def dfs(root, mi, ma):
            if root == None:
                return 0
            diff = max(abs(root.val - mi), abs(root.val - ma))
            mi = min(mi, root.val)
            ma = max(ma, root.val)
            diff = max(diff, dfs(root.left, mi, ma))
            diff = max(diff, dfs(root.right, mi, ma))
            return diff
        return dfs(root, root.val, root.val)
