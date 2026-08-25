# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0

        def _dfs(root, depth):

            if not root.left and not root.right:
                return depth

            left_depth = 0
            if root.left:
                left_depth = _dfs(root.left, depth + 1)

            right_depth = 0
            if root.right:
                right_depth = _dfs(root.right, depth + 1)
            
            return max(right_depth, left_depth)

        return _dfs(root, 1)