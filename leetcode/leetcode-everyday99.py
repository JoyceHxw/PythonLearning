# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def nextLargerNodes(self, head: ListNode) -> list[int]:
        # 暴力超时
        # ans=[]
        # while head!=None:
        #     node=head.next
        #     while node!=None and node.val<=head.val:
        #         node=node.next
        #     if node!=None:
        #         ans.append(node.val)
        #     else:
        #         ans.append(0)
        #     head=head.next
        # return ans

        # 单调栈
        values=[]
        while head!=None:
            values.append(head.val)
            head=head.next
        ans=[0]*len(values)
        stk=[]
        i=len(values)-1
        # 从后往前维护单调递减的栈
        while i>=0 or stk!=[]:
            if stk==[] or (i>=0 and values[i]<stk[-1]):
                if stk!=[]:
                    ans[i]=stk[-1]
                stk.append(values[i])
                i-=1
            else:
                stk.pop()
        return ans