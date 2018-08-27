# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack = []
        self.next_min = None
        self.min_num = None
        self.is_top = True

    def push(self, node):
        # write code here
        if self.min_num and node < self.min_num:
            self.is_top = True
            self.next_min = self.min_num
            self.min_num = node
        elif not self.min_num:
            self.min_num = node
        else:
            self.is_top = False
        self.stack.append(node)

    def pop(self):
        # write code here
        if 


    def top(self):


    def min(self):
        # write code here




u = Solution()
u.push(3)
print(u.min())
u.push(4)
print(u.min())
u.push(2)
print(u.min())
u.pop()
print(u.min())