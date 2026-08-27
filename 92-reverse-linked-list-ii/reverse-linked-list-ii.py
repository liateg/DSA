# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head

        cur = head
        left_n = ListNode(0)
        l = None
        r = None
        i = 1

        # Handle the case where the reversal starts at the head
        if left == 1:
            left_n.next = head

        while cur and i <= right:
            if i + 1 == left:
                left_n.next = cur.next
                l = cur
            if i == right:
                r = cur.next
            cur = cur.next
            i += 1

        pre = None
        cur = left_n.next
        ll = cur  # original left node (becomes the tail)

        while cur and cur != r:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt

        if left == 1:
            head = pre
        else:
            l.next = pre

        ll.next = r

        return head