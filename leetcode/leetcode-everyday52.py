# 给你两个链表 list1 和 list2 ，它们包含的元素分别为 n 个和 m 个。
# 请你将 list1 中下标从 a 到 b 的全部节点都删除，并将list2 接在被删除节点的位置。


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 注意listnode用法，节点指向
# 注意变量变化关系
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        preA = list1
        for _ in range(a - 1):
            preA = preA.next
        preB = preA
        for _ in range(b - a + 2):
            preB = preB.next
        preA.next = list2
        while list2.next:
            list2 = list2.next
        list2.next = preB
        return list1
