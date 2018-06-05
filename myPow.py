class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n==0:
            return 1
        elif n==1:
            return x
        elif n<0:
            return 1/(self.myPow(x,-n//2)*self.myPow(x,-n+n//2))
        elif n%2:
            return x*self.myPow(x,n-1)
        return self.myPow(x*x,n//2)


u = Solution()
test = [
    1


]

for x in test:
    print(u.myPow(3.2,2))
