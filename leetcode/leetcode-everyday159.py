# 给你一个链表数组，每个链表都已经按升序排列。
# 请你将所有链表合并到一个升序链表中，返回合并后的链表。

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: list[ListNode]) -> ListNode:
        # 选定一个为起始链表，后续链表分别插入其中
        if len(lists)==0:
            return None
        # 以parent为参考，因为可能添加头节点
        parent=ListNode()
        k=0
        ans=lists[k]
        while k<len(lists):
            if lists[k]!=None:
                ans=lists[k]
                break
            k+=1
        parent.next=ans
        parent_temp=parent
        for i in range(k+1,len(lists)):
            cur=lists[i]
            temp=parent.next
            while cur!=None and temp!=None:
                while cur!=None and temp!=None and cur.val>=temp.val:
                    temp=temp.next
                    parent_temp=parent_temp.next
                t=cur.next
                parent_temp.next=cur
                # 直接续上链表
                if temp!=None:
                    cur.next=temp
                cur=t
                parent_temp=parent_temp.next
            parent_temp=parent
        return parent.next

n1=ListNode(-1)
n2=ListNode(1)
n1.next=n2
l1=n1

m1=ListNode(-3)
m2=ListNode(1)
m3=ListNode(4)
m1.next=m2
m2.next=m3
l2=m1

k1=ListNode(-2)
k2=ListNode(-1)
k3=ListNode(0)
k4=ListNode(2)
k1.next=k2
k2.next=k3
k3.next=k4
l3=k1

S=Solution()
S.mergeKLists([l1,l2,l3])
