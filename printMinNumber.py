class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        str_list = []
        length = 0
        for i in numbers:
            str_i = str(i)
            length = max(length,len(str_i))
            str_list.append(str_i)
        full_str_dict = {}
        for i in str_list:
            str_full = ""
            if len(i) < length:
                str_full += i[0] * (length-len(i))
            str_full += i
            if str_full in full_str_dict.keys():
                full_str_dict[str_full] += i
            else:
                full_str_dict[str_full] = i
        keys = full_str_dict.keys()
        keys = sorted(keys)
        all_str = ""
        for i in keys:
            all_str += full_str_dict[i]
        return int(all_str)
u = Solution()
print(u.PrintMinNumber([1,11,111]))