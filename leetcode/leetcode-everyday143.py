# 给定一个有 N 个结点的二叉树的根结点 root，树中的每个结点上都对应有 node.val 枚硬币，并且总共有 N 枚硬币。
# 在一次移动中，我们可以选择两个相邻的结点，然后将一枚硬币从其中一个结点移动到另一个结点。(移动可以是从父结点到子结点，或者从子结点移动到父结点。)。
# 返回使每个结点上只有一枚硬币所需的移动次数。

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 自己写出的dfs，但基本花了一个上午才理清
# 可以双向移动，计算时用正负值代表方向
class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        ans=0
    
        def dfs(node):
            if node==None:
                return
            step=0
            dfs(node.left)
            dfs(node.right)
            # 更新每个节点的硬币数量（正值代表多余，负值代表缺少）
            step+=0 if node.left==None else node.left.val-1 #需要给左子节点的硬币
            step+=0 if node.right==None else node.right.val-1 #需要给右子节点的硬币
            node.val+=step
            # 加总移动的硬币数
            nonlocal ans
            ans+=abs(0 if node.left==None else node.left.val-1)
            ans+=abs(0 if node.right==None else node.right.val-1)
            return

        dfs(root)
        return ans