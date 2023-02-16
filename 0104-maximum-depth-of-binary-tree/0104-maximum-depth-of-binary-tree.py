# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        visted = []
        head = root
        maxDepth = 0
        currentCount = 1
        while head:    
            currentCount+= 1
            if head.right:
                visted.append({currentCount: head.right})
            else: 
                maxDepth = max(maxDepth, currentCount - 1)
                if len(visted) == 0 and not head.left : break
            if head.left:
                head = head.left
            else: 
                maxDepth = max(maxDepth, currentCount - 1)
               
                if len(visted) > 0:
                    Map = visted.pop()
                    arr = [key for key in Map]
                    head = Map[arr[0]]
                    currentCount = arr[0]
        return max(maxDepth, currentCount - 1)



            
        