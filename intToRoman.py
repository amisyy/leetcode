class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        dicts = [["I",1],["V",5],["X",10],["L",50],["C",100],["D",500],["M",1000]]
        length = 7
        i = 1
        if num ==0:
            return ""
        if num >=1000:
            return dicts[6][0] + self.intToRoman(num -1000)
        while i <7:
            if dicts[i-1][1] <= num and num < dicts[i][1]:
                if (i==1 or i ==3 or i==5) and num >= dicts[i][1] - dicts[i-1][1] :
                    return dicts[i-1][0] + dicts[i][0] +self.intToRoman(num - (dicts[i][1] - dicts[i-1][1]))
                elif (i==2 or i==4  or i==6) and num >= dicts[i][1] - dicts[i-2][1]:
                    return dicts[i-2][0] + dicts[i][0] +self.intToRoman(num - (dicts[i][1] - dicts[i-2][1]))
                else:
                    return dicts[i-1][0] + self.intToRoman(num - dicts[i-1][1])
            else:
                i+=1

u = Solution()
print(u.intToRoman(2000))
