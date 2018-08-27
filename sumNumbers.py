# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        sum = 0
        cur = [root]
        next = []
        while cur:
            for now in cur:
                if now is None:
                    return 0
                else:
                    if now.left is None and now.right is None:
                        sum += now.val
                    else:
                        if now.left is not None:
                            now.left.val = now.val * 10 + now.left.val
                            next.append(now.left)
                        if now.right is not None:
                            now.right.val = now.val * 10 + now.right.val
                            next.append(now.right)
            cur = next
            next = []
        return sum

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
u = Solution()
print(u.sumNumbers(root))


