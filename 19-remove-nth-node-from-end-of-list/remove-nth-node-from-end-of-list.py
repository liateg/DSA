# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        cur=head
        l=0
        while cur:
            l+=1
            cur=cur.next
        if n==1 and l==1:
            return
        j=l-n
        if j==0:
            head=head.next
            return head
        cur=head
        for i in range(j-1):
            cur=cur.next
        if cur.next:
            cur.next=cur.next.next
        else:
            cur.next=None
        return head

