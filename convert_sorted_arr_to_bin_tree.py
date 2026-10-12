# Definition for a binary tree node.
# class TreeNode:
#     def init(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution: 
    def buildBST(self, nums, start, end) -> TreeNode | None: 
        # base case 
        if start > end: 
            return None
        mid = (start + end) // 2
        root = TreeNode(val=nums[mid])
        root.left = self.buildBST(nums, start, mid-1)
        root.right = self.buildBST(nums, mid+1, end)
        return root
    

    def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:
        return self.buildBST(nums, 0, len(nums)-1)