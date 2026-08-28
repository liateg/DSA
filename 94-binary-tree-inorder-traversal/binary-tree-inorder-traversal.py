# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        lob=[]
        ino=[]
        cur=root

        while cur or lob:
            while cur:
                lob.append(cur)
                cur=cur.left
            ino.append(lob[-1].val)
            cur=lob[-1].right
            lob.pop()
        return ino

