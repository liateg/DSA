# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur=head
        l=0
        while cur:
            cur=cur.next
            l+=1
        cur=head
        for i in range(int(l/2)):
            cur=cur.next
        return cur 
