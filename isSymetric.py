# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def isSymetricTree(self,tree1,tree2):
        if not tree1.val == tree2.val:
            return False
        left_flag = False
        right_flag = False
        if tree1.left is not None and tree2.right is not None:
            left_flag = self.isSymetricTree(tree1.left,tree2.right)
        if tree1.left is None and tree2.right is None:
            left_flag = True
        if tree2.left is not None and tree1.right is not None:
            right_flag = self.isSymetricTree(tree2.left,tree1.right)
        if tree2.left is None and tree1.right is None:
            right_flag = True
        return left_flag and right_flag
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        else:
            if root.left is not None and root.right is not None:
                return self.isSymetricTree(root.left,root.right)
            elif root.left is None and root.right is None:
                return True
            else:
                return False






u = Solution()



test = [
1
]

for x in test:
    print(u.isInterleave("aa","ab","abaa"))




