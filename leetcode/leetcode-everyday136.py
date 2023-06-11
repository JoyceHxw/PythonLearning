# 给你一个链表的头节点 head，请你编写代码，反复删去链表中由 总和 值为 0 的连续节点组成的序列，直到不存在这样的序列为止。
# 删除完毕后，请你返回最终结果链表的头节点。


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        # 栈，复杂度大于O(n)，并且需要重新建立链表
        # ans=[0]*1000
        # top=0
        # while head!=None:
        #     if head.val==0:
        #         head=head.next
        #         continue
        #     if top==0:
        #         ans[top]=head.val
        #         top+=1
        #     else:
        #         temp=top-1
        #         s=ans[temp]
        #         while temp>=0 and s+head.val!=0:
        #             temp-=1
        #             s+=ans[temp]
        #         if s+head.val==0:
        #             top=temp
        #         else:
        #             ans[top]=head.val
        #             top+=1
        #     head=head.next
        # node=ListNode()
        # root=node
        # # print(top)
        # for i in range(top):
        #     t=ListNode()
        #     t.val=ans[i]
        #     node.next=t
        #     node=node.next
        # return root.next

        # 答案：前缀和+哈希表（对前缀和的理解）
        # 前缀和相同，说明中间部分的和为0
        dummy = ListNode(next=head)
        last = {}
        s, cur = 0, dummy
        while cur:
            s += cur.val
            last[s] = cur
            cur = cur.next
        s, cur = 0, dummy
        while cur:
            s += cur.val
            cur.next = last[s].next
            cur = cur.next
        return dummy.next
            