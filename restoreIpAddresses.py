class Solution(object):
    def restore(self,s,n):
        if not s:
            return False
        if n==1:
            if ((not s == "") and int(s)<=255) or s=="0":
                return [s]
            else:
                return False
        else:
            result = []
            temp1 = self.restore(s[1:], n - 1)
            if s[0]=="0":
                if temp1:
                    return [s[:1]+"."+i for i in temp1]
                else:
                    return False
            temp2 = self.restore(s[2:],n-1)
            if int(s[:3])<=255:
                temp3 = self.restore(s[3:],n-1)
            else:
                temp3 = False
            if temp1:
                result.extend([s[:1]+"."+i for i in temp1])
            if temp2:
                result.extend([s[:2] + "." + i for i in temp2])
            if temp3:
                result.extend([s[:3] + "." + i for i in temp3])
            if len(result) == 0:
                return False
            else:
                return result


    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = self.restore(s,4)
        if result:
            return result
        else:
            return []





u = Solution()



test = [
"25525511135",
"",
"0000",
"0"
]

for x in test:
    print(u.restoreIpAddresses(x))




