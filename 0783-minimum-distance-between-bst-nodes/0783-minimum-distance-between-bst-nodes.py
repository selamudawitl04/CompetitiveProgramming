# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.stack = []
    def inorderTraversal(self, root) -> list:
        if not root: return
        self.inorderTraversal(root.left)
        self.stack.append(root.val)
        self.inorderTraversal(root.right)

    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.inorderTraversal(root)
        minValue = float(inf)
        for i in range(len(self.stack) - 1):
            minValue = min(minValue, self.stack[i + 1] - self.stack[i])
        return minValue

      
        
        