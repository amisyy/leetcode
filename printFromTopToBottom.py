class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if root is not None:
            return self.getNextlist([root],[root.val])
        else:
            return []
    def getNextlist(self,thisList,retList):
        nextList = []
        for i in thisList:
            if i.left is not None:
                retList.append(i.left.val)
                nextList.append(i.left)
            if i.right is not None:
                retList.append(i.right.val)
                nextList.append(i.right)
        if nextList:
            retList = self.getNextlist(nextList,retList)
        return retList

a = TreeNode(1)
a.left = TreeNode(2)
a.right = TreeNode(3)
u = Solution()
print(u.PrintFromTopToBottom(a))
