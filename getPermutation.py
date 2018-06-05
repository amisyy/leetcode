class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        import math
        num_list = [i+1 for i in range(n)]
        mod_num = k
        result = []
        for i in range(n-1):
            fac = math.factorial(n - i - 1)
            result.append(num_list[(mod_num-1)//fac])
            del num_list[(mod_num-1)//fac]
            mod_num = (mod_num-1) % fac + 1

        result.append(num_list[0])
        return result


u = Solution()

test = [
1


]


for x in test:
    print(u.getPermutation(4,6))


