# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        
        def helper(node):
            if not node:
                return (True, float('inf'), float('-inf'), 0)
            
            left_is_bst, left_min, left_max, left_sum = helper(node.left)
            right_is_bst, right_min, right_max, right_sum = helper(node.right)
            
            if left_is_bst and right_is_bst and node.val > left_max and node.val < right_min:
                current_sum = node.val + left_sum + right_sum
                self.max_sum = max(self.max_sum, current_sum)
                return (True, min(node.val, left_min), max(node.val, right_max), current_sum)
            else:
                return (False, 0, 0, 0)
        
        self.max_sum = 0
        helper(root)
        return self.max_sum