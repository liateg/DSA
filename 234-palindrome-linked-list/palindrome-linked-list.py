# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        tem=head
        val=[]
        while tem:
            val.append(tem.val)
            tem=tem.next
        return val==val[::-1]

