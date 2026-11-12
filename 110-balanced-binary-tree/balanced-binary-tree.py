# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        def f(root):
            if not root:
                return [True,0]
            l_b,l_h = f(root.left)
            r_b,r_h = f(root.right)
            i_b = l_b and r_b and abs(l_h-r_h)<=1
            return [i_b,1+max(l_h,r_h)]
        return f(root)[0]