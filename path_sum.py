# Definition for a binary tree node.
# class TreeNode:
#     def init(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution: 
    def check(self, node, sum, targetSum) -> bool: 
        if not node.left and not node.right: 
            sum += node.val 
            if sum == targetSum: 
                return True 
            return False 
        elif node.left and not node.right: 
            return self.check(node.left, sum + node.val, targetSum) 
        elif not node.left and node.right: 
            return self.check(node.right, sum + node.val, targetSum) 
        else: 
            return self.check(node.left, sum + node.val, targetSum) or self.check(node.right, sum + node.val, targetSum)

    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        if not root:
            return False
        return self.check(root, 0, targetSum)