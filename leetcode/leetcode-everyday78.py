# 给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。
# 请你将两个数相加，并以相同形式返回一个表示和的链表。
# 你可以假设除了数字 0 之外，这两个数都不会以 0 开头。

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        print(l1)
        digit1=0
        digit2=0
        s1=l1
        s2=l2
        num1=0
        num2=0
        while s1!=None:
            num1+=s1.val*(10**digit1)
            s1=s1.next
            digit1+=1
        while s2!=None:
            num2+=s2.val*(10**digit2)
            s2=s2.next
            digit2+=1
        sum_num=num1+num2
        sum_str=str(sum_num)
        print(sum_str)
        i=0
        while i<len(sum_str):
            l3=ListNode(int(sum_str[i]))
            if i==0:
                l3.next=None
            else:
                l3.next=temp
            temp=l3
            i+=1
        print(l3)
        return l3