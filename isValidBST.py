# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        min = -float('Inf')
        max = float('Inf')
        return self.validBST(root,min,max)
    def validBST(self,root,min,max):
        if root is None:
            return True
        else:
            if root.left is not None:
               if root.left.val < root.val and root.left.val > min:
                   new_max = root.val
                   new_min = min
                   if self.validBST(root.left,new_min,new_max):
                        left = True
                   else :
                        left = False
               else:
                   left = False
            else:
                left = True
            if root.right is not None:
                if root.right.val > max and root.right.val < max:
                    new_max = max
                    new_min = root.val
                    if self.validBST(root.right,new_min,new_max):
                        right = True
                    else:
                        right = False
                else:
                    right = False
            else:
                right = True
            return right and left



u = Solution()



test = [
1
]

for x in test:
    print(u.isInterleave("aa","ab","abaa"))




