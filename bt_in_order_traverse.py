# Definition for a binary tree node.
# class TreeNode:
# def init(self, val=0, left=None, right=None):
# self.val = val
# self.left = left
# self.right = right
class Solution: 
    def inorderTraversal(self, root: TreeNode | None) -> list[int]: 
        out = [] 
        s = [] 
        i = root 
        while i or s: 
            # left first 
            while i: 
                s.append(i) 
                i = i.left
                
            # no more left, pop print
            i = s.pop()
            out.append(i.val)
            
            # go right
            i = i.right
            
        return out