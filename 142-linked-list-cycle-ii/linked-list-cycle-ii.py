# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur=head
        review=set()
        while cur and cur.next:
            if cur.next in review:
                return cur.next
            review.add(cur)
            cur=cur.next
        return None