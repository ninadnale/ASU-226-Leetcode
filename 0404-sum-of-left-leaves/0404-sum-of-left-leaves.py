# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        left = []
        right = [root]
        total = 0

        while(left or right):
            tempL = []
            tempR = []
            while left:
                node = left.pop(0)
                if(node.left):
                    tempL.append(node.left)
                if(node.right):
                    tempR.append(node.right)
                if(not node.left and not node.right):
                    total += node.val
            
            while right:
                node = right.pop(0)
                if(node.left):
                    tempL.append(node.left)
                if(node.right):
                    tempR.append(node.right)
            
            left = tempL
            right = tempR
            # print(left, right)
        
        return total
        