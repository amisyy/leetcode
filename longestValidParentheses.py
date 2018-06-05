class Solution(object):
    def longestValidParentheses(self, s):
        core_list = {}
        cur = -1
        length = len(s)
        if length<2:
            return 0
        while True:
            cur = s.find("()",cur+1)
            if cur==-1:
                break
            core_list[cur] = 2
        if not core_list:
            return 0
        merged = True
        while merged :
            merged = False
            key_list = sorted(core_list.keys())
            for i in range(len(key_list)-1):
                if key_list[i] + core_list[key_list[i]] == key_list[i+1]:
                    core_list[key_list[i]] = core_list[key_list[i]] + core_list[key_list[i+1]]
                    del core_list[key_list[i+1]]
                    key_list[i+1] = key_list[i]
                    merged = True
            key_list = sorted(list(set(key_list)))
            for i in range(len(key_list)):
                left = key_list[i]
                right = key_list[i] + core_list[key_list[i]] -1
                while True:
                    if left<1 or right>length-2:
                        break
                    if s[left-1] == "(" and s[right+1] == ")":
                        left -= 1
                        right += 1
                        core_list[left] = (right-left) + 1
                        merged = True
                        del core_list[left+1]
                    else:
                        break
        return max(core_list.values())






u = Solution()
test = [
    '()',
    ')(',
    '((()()()()',
    '))))()))))()))))',
    '((((()))))',
    '((((()((())',
    '))()(()()(()()))((()',
    ''
]
for x in test:
    print(u.longestValidParentheses(x))
