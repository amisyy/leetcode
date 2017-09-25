class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        MAX_INT = 2147483647

        if divisor ==0:
            return -1
        minus = False
        if dividend <0 and divisor>0 :
            minus = True
            dividend = -dividend
        elif dividend>0 and divisor<0:
            minus = True
            divisor = -divisor
        else:
            dividend = abs(dividend)
            divisor = abs(divisor)
        i = 0
        while dividend>=divisor:
            temp = divisor
            swift = 1
            while temp+temp<dividend:
                temp = temp+temp
                swift = swift+swift
            dividend-=temp
            i+= swift
        if minus:
            return -i
        return i




u = Solution()
print(u.divide(18,3))
