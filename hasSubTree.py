class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if pRoot2 is None:
            return False
        while pRoot1 is not None and pRoot2 is not None:
            if pRoot1.val == pRoot2.val:
                if self.sameTree(pRoot1.left, pRoot1.left) and self.sameTree(pRoot1.right, pRoot2.right):
                    return True
            return self.HasSubtree(pRoot1.left, pRoot2) or self.HasSubtree(pRoot1.right, pRoot1)

    def sameTree(self, tree1, tree2):
        if tree2 is None:
            return True
        while tree2 is not None:
            if not tree1.val == tree2.val:
                return False
            else:
                return self.sameTree(tree1.left, tree2.left) and self.sameTree(tree1.right, tree2.right)
