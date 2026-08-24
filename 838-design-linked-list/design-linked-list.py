class ListNode:
    def __init__(self,val):
        self.val=val
        self.pre=None
        self.next=None
class MyLinkedList:

    def __init__(self):
        self.left=ListNode(0)
        self.right=ListNode(0)
        self.right.pre=self.left
        self.left.next=self.right

    def get(self, index: int) -> int:

        cur=self.left.next
        while cur and index>0:
            cur=cur.next
            index-=1
        if index==0 and cur != self.right and cur:
            return cur.val
        return -1
        

    def addAtHead(self, val: int) -> None:
        cur=ListNode(val)
        cur.next=self.left.next
        cur.pre=self.left
        self.left.next.pre=cur
        self.left.next=cur
        

    def addAtTail(self, val: int) -> None:
        cur=ListNode(val)
        cur.next=self.right
        cur.pre=self.right.pre
        self.right.pre.next=cur
        self.right.pre=cur



    def addAtIndex(self, index: int, val: int) -> None:
        cur=self.left.next
        while cur and index>0:
            cur=cur.next
            index-=1
        if index==0 and cur:
            temp=ListNode(val)
            temp.pre=cur.pre
            temp.next=cur
            
            cur.pre.next=temp
            cur.pre=temp

        

    def deleteAtIndex(self, index: int) -> None:
        cur=self.left.next
        while cur and index>0:
            cur=cur.next
            index-=1
        if index==0 and cur and cur !=self.right:
            cur.pre.next=cur.next
            cur.next.pre=cur.pre


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)