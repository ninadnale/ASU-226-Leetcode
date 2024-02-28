# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        queue = [root]
        prev_left = [root]
        while queue:
            temp_que = []
            for node in queue:
                if(node.left):
                    temp_que.append(node.left)
                if(node.right):
                    temp_que.append(node.right)
            queue = temp_que
            if(temp_que):
                prev_left = temp_que
        
        return prev_left.pop(0).val