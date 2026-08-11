# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def _dfs(root, depth):
            if root is None:
                return depth

            print(depth)
            left = _dfs(root.left, depth + 1) if root.left else depth
            right = _dfs(root.right, depth + 1) if root.right else depth

            return max(left, right)

        if not root:
            return 0
        return _dfs(root, 1)