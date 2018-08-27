# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        stack1 = []
        stack2 = popV
        cur = 0
        for i in range(len(pushV)):
            stack1.append(pushV[i])
            while stack1 and stack1[-1] == stack2[cur]:
                cur += 1
                stack1.pop()
        if not stack1 and cur == len(stack2):
            return True
        else:
            return False


u = Solution()
print(u.IsPopOrder([1, 2, 3, 4, 5], [4, 3, 5, 1, 2]))
