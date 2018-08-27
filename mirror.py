class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        if root is None:
            return None
        temp = TreeNode(root.val)
        temp.left = self.Mirror(root.right)
        temp.right = self.Mirror(root.left)
        root = temp
        return root
a = TreeNode(8)
left = TreeNode(6)
right = TreeNode(10)
left.left = TreeNode(5)
left.right = TreeNode(7)
right.left = TreeNode(9)
right.right = TreeNode(11)
a.left = left
a.right = right
u = Solution()
print(u.Mirror(a).left.val)