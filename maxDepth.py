# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


class Solution(object):
    def levelList(self, root_list,flag):
        result = []

        for i in root_list[-1]:
            if i.left is not None:
                result.append(i.left)
            if i.right is not None:
                result.append(i.right)
        for i in result:
            print(i.val)
        if not len(result) == 0:
            if not flag:
                result = list(reversed(result))
            root_list.append(result)
            new_root_list = self.levelList(root_list,not flag)
            return new_root_list
        return root_list


    def maxDepth(self, root):

        if root is None:
            return 0
        else:
            result = self.levelList([[root]],True)
            return len(result)








u = Solution()



test = [
1
]

for x in test:
    print(u.isInterleave("aa","ab","abaa"))




