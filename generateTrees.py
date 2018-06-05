# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def gener(self,list_):
        length = len(list_)
        if length==1:
            return [TreeNode(list_[0])]
        elif length == 0:
            return [None]
        else:
            result = []
            for i in range(length):
                result_temp = []
                left_list = list_[:i]
                right_list = list_[i+1:]
                if not len(left_list)==0:
                    left_node = self.gener(left_list)
                else:
                    left_node = [None]
                if len(right_list)==0:
                    right_node = [None]
                else:
                    right_node = self.gener(right_list)

                for j in left_node:
                    for k in right_node:
                        root_node = TreeNode(list_[i])
                        root_node.left = j
                        root_node.right = k
                        result_temp.append(root_node)
                result.extend(result_temp)
            return result


    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        list_ = [i+1 for i in range(n)]
        return self.gener(list_)



u = Solution()



test = [
3
]

for x in test:
    print(u.generateTrees(x))




