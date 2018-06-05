class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        if length == 0 or s[0] == "0":
            return 0
        elif length == 1:
            return 1
        elif length == 2:
            if (int(s)>26 and s[1]!="0") or (int(s)<=26 and s[1]=="0"):
                return 1
            elif int(s)>26 and s[1]=="0":
                return 0
            return 2
        else:
            if s[-1]=="0" and s[-2]=="0":
                return 0
            elif s[-1]=="0":
                if int(s[-2])>2:
                    return 0
                else:
                    return self.numDecodings(s[:length-2])
            elif s[-2] == "0":
                if int(s[-3])>2:
                    return 0
                elif int(s[-3])==0:
                    return 0
                return 1 if length==3 else self.numDecodings(s[:length-3])
            if int(s[length - 3:length-1]) > 26 and int(s[length - 2:]) > 26:
                return self.numDecodings(s[:length-2])
            elif int(s[length - 2:]) > 26:
                return self.numDecodings(s[:length-1])
            elif int(s[length - 3:length-1]) > 26:
                return self.numDecodings(s[:length-2]) * 2
            else:
                return self.numDecodings(s[:length-2])+self.numDecodings(s[:length-1])



u = Solution()



test = [
"1001",
"101",
"1234",
"1326",
"1226",
"3416352693542631413"
]

for x in test:
    print(u.numDecodings(x))




