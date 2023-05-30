# 给出二叉树的根节点 root，树上每个节点都有一个不同的值。
# 如果节点值在 to_delete 中出现，我们就把该节点从树上删去，最后得到一个森林（一些不相交的树构成的集合）。
# 返回森林中的每棵树。你可以按任意顺序组织答案。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 难点在于，删除当前节点需要使父节点指向空指针，所以采用返回值的方式
class Solution:
    def delNodes(self, root: TreeNode, to_delete: list[int]) -> list[TreeNode]:
        ans=[]
        # 从叶子节点到根节点分离（后序遍历）
        def dfs(root: TreeNode):
            if root==None:
                return None
            root.left=dfs(root.left)
            root.right=dfs(root.right)
            nonlocal ans
            for n in to_delete:
                if root.val==n:
                    if root.left!=None:
                        ans.append(root.left)
                    if root.right!=None:
                        ans.append(root.right)
                    return None
            return root
        if dfs(root)!=None:
            ans.append(root)
        return ans