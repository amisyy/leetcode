class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        import re
        path_split = re.split('[/*]',path)
        length = len(path_split)
        result_split = []
        for i in range(length):
            if path_split[i] == ""  or path_split[i] == '.'   :
                continue
            elif path_split[i]=='..':
                if not result_split == []:
                    result_split.pop()
                else:
                    continue
            else:
                result_split.append(path_split[i])
        result = ''
        for i in result_split:
            result = result + '/' + i
        if result=='':
            return '/'
        return result



u = Solution()

test = [
    '/a/./b/../c/',
    '/a/./b/c/',
    '/../',
    "/a/./b/../../c/"
]
for x in test:
    print(u.simplifyPath(x))



