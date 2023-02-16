# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        visted = deque()
        result = []
        head = root
        depth = 0
        visted.append({depth: head}) 
        while head and len(visted) > 0:
            poppedNodeWithDepth = visted.popleft()
            depth = [key for key in poppedNodeWithDepth][0]
            # print(depth)
            head = poppedNodeWithDepth[depth]
            # print(visted)
            if len(result) <= depth:
                result.append([head.val])
            else:
                result[depth].append(head.val)
            if head.left and head.right:
                visted.append({depth + 1 : head.left})
                visted.append({depth + 1 : head.right})
            elif head.left:
                visted.append({depth + 1 : head.left})
            elif head.right:
                visted.append({depth + 1 : head.right})
        return result
                
    
            
        