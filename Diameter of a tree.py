# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def DFS(root):
            nonlocal res
            if not root:
                return 0
            left = DFS(root.left)
            right = DFS(root.right)
            res = max(res,left+right)
            return 1+max(left,right)
        DFS(root)
        return res
''' 
Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
Example 2:

Input: root = [1,2]
Output: 1
 
'''
