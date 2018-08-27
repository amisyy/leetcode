# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        num_list = [i for i in range(1, n + 1)]
        return list(set(self.generrate(num_list)))

    def generrate(self, num_list):
        ret = []
        if not num_list:
            return [None]
        for i in range(len(num_list)):
            left_tree_nodes = self.generrate(num_list[:i])
            right_tree_nodes = self.generrate(num_list[i + 1:])
            for left_node in left_tree_nodes:
                for right_node in right_tree_nodes:
                    root = TreeNode(num_list[i])
                    root.left = left_node
                    root.right = right_node
                    ret.append(root)
        if not ret:
            return [None]
        return ret


u = Solution()
print(u.generateTrees(3))
