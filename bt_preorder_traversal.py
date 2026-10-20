# Definition for a binary tree node.
# class TreeNode:
# def init(self, val=0, left=None, right=None):
# self.val = val
# self.left = left
# self.right = right
class Solution: 
    def preorderTraversal(self, root: TreeNode | None) -> list[int]:
        if not root:
            return []
        # mimic call stack of recursive
        out = []
        stack = [root]
        while stack:
            # print first
            i = stack.pop()
            out.append(i.val)
            
            # push right first so left pops first
            if i.right:
                stack.append(i.right)
            if i.left:
                stack.append(i.left)
            
        return out