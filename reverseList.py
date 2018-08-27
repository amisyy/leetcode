# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        stack = []
        temp = pHead
        while temp is not None:
            stack.append(temp)
            temp = temp.next
        if stack:
            new_temp = ListNode(stack.pop())
            new_head = new_temp
            while stack:
                new_temp.next = ListNode(stack.pop())
                new_temp = new_temp.next
            print(new_head)
            return new_head
        else:
            return None

before = ListNode(1)
a = before
for i in range(1,5):
    temp = ListNode(i)
    before.next = temp
    before = before.next
while a is not None:
    print(a.val)
    a = a.next
