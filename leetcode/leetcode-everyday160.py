# 给你两棵二叉树： root1 和 root2 。
# 想象一下，当你将其中一棵覆盖到另一棵之上时，两棵树上的一些节点将会重叠（而另一些不会）。你需要将这两棵树合并成一棵新二叉树。合并的规则是：如果两个节点重叠，那么将这两个节点的值相加作为合并后节点的新值；否则，不为 null 的节点将直接作为新二叉树的节点。
# 返回合并后的二叉树。
# 注意: 合并过程必须从两个树的根节点开始。

 

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        # 相同遍历
        # if root1!=None and root2!=None:
        #     root1.val+=root2.val
        # elif root1!=None and root2==None:
        #     root2=TreeNode(root1.val)
        # elif root1==None and root2!=None:
        #     root1=TreeNode(root2.val)
        # else:
        #     return None

        # def dfs(root1,root2):
        #     if root1==None and root2==None:
        #         return

        #     if root1.left==None and root2.left!=None:
        #         root1.left=TreeNode(root2.left.val)
        #     elif root1.left!=None and root2.left==None:
        #         root2.left=TreeNode(root1.left.val)
        #     elif root1.left!=None and root2.left!=None:
        #         root1.left.val+=root2.left.val
        #     dfs(root1.left,root2.left)

        #     if root1.right==None and root2.right!=None:
        #         root1.right=TreeNode(root2.right.val)
        #     elif root1.right!=None and root2.right==None:
        #         root2.right=TreeNode(root1.right.val)
        #     elif root1.right!=None and root2.right!=None:
        #         root1.right.val+=root2.right.val
        #     dfs(root1.right,root2.right)

        # dfs(root1,root2)
        # return root1

        # 代码优化，利用返回变量
        if not root1:
            return root2
        if not root2:
            return root1
        merged=TreeNode(root1.val+root2.val)
        merged.left=self.mergeTrees(root1.left,root2.left)
        merged.right=self.mergeTrees(root1.right,root2.right)
        return merged