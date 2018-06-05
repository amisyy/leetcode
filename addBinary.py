class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        m = len(a)
        n = len(b)
        result = ""
        c = 0
        if m>n:
            b = "0"*(m-n) + b
        else:
            a = "0"*(n-m) + a
        for i in range(max(m,n)):
            temp = int(a[-i-1]) + int(b[-i-1]) + c
            if temp>=2:
                c = 1
                temp -= 2
            else:
                c = 0
            result += str(temp)
        if c:
            result = str(c) + result[::-1]
        else:
            result = result[::-1]
        return  result



u = Solution()

test = [
    1
]
for x in test:
    print(u.addBinary('11','1'))



