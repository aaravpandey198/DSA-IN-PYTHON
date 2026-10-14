# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        ans = []
        temp = head
        while temp:
            ans.append(temp.val)
            temp = temp.next
        return ans == ans[::-1]