#Definition for a binary tree node.
#class TreeNode(object):
#   def __init__(self,x)
#       self.val = x
#       self.left = None
#       self.right = None


class Solution(object):
    def hasPathSum(self,root,sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None:
            return False
        left,right = False,False
        if root.left is not None:
                left = left or self.hasPathSum(root.left,sum-root.val)
        if root.right is not None:
                right = right or self.hasPathSum(root.right,sum-root.val)
        if root.left is None and root.right is None:
            if root.val == sum:
                return True
            else:
                return False
        return left or right


