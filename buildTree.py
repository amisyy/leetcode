# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        length = len(preorder)
        if length == 0:
            return None
        elif length == 1:
            return TreeNode(preorder[0])
        else:
            root_val = preorder[0]
            root = TreeNode(root_val)
            root_index = inorder.index(root_val)
            left_preorder = preorder[1:root_index+1]
            right_preorder = preorder[root_index+1:]
            left_inorder = inorder[0:root_index]
            right_inorder = inorder[root_index+1:]
            left = self.buildTree(left_preorder,left_inorder)
            right = self.buildTree(right_preorder,right_inorder)
            root.left = left
            root.right = right
            return root










u = Solution()



test = [
1
]

for x in test:
    print(u.isInterleave("aa","ab","abaa"))




