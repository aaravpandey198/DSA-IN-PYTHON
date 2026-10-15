# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        seen = []
        while temp:
            if temp in seen:
                return temp
            seen.append(temp)
            temp = temp.next
        return None