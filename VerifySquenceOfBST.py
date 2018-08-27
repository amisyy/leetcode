# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        length = len(sequence)
        if not sequence:
            return False
        if length == 1 or length == 2:
            return True
        elif length == 3:
            if sequence[0] <= sequence[2] and sequence[1] >= sequence[2]:
                return True
            else:
                return False
        else:
            less = []
            more = []
            less_is_full = False
            for i in range(length - 1):
                if sequence[i] <= sequence[-1]:
                    less.append(sequence[i])
                else:
                    less_is_full = True
                if less_is_full:
                    if sequence[i] >= sequence[-1]:
                        more.append(sequence[i])
                    else:
                        return False
            left = True if not less or self.VerifySquenceOfBST(less) else False
            right = True if not more or self.VerifySquenceOfBST(more) else False

            return left and right
u = Solution()
print(u.VerifySquenceOfBST([1,2,3,4,5]))