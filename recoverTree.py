# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """

        pre_cur = None
        pre = None
        p1 = None
        p2 = None
        cur = root
        found = False
        while cur is not None:
            if cur.left is None:
                if pre_cur is not None and pre_cur.val>cur.val:
                    if not found:
                        found = True
                        p1 = pre_cur
                    p2 = cur
                pre_cur = cur
                cur = cur.right
            else:
                pre = cur.left
                while pre.right is not None and not pre.right == cur:
                    pre = pre.right
                if pre.right is None:
                    pre.right = cur
                    cur = cur.left
                else:
                    if pre_cur is not None and pre_cur.val > cur.val:
                        if not found:
                            found = True
                            p1 = pre_cur

                        p2 = cur
                    pre_cur = cur
                    pre.right = None
                    cur = cur.right
        if p1 is not None and p2 is not None:
            temp = p1.val
            p1.val = p2.val
            p2.val = temp





u = Solution()



test = [
1
]

for x in test:
    print(u.isInterleave("aa","ab","abaa"))




