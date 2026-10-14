# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        n = 0
        temp = head
        while temp is not None:
            temp = temp.next
            n += 1
        temp = head
        for _ in range(0, n // 2):
            temp = temp.next
        return temp
