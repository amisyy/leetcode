class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        neg = 0 if numerator * denominator > 0 else 1
        numerator, denominator = abs(numerator), abs(denominator)
        not_the_same = True
        mod_list = []
        div_list = []
        int_part = numerator // denominator
        repeat_start = 0
        if numerator % denominator == 0:
            is_int = True
        else:
            is_int = False
        frac_num = 0
        frac = numerator
        while not_the_same:
            frac = frac % denominator
            if frac == 0:
                break
            if frac not in mod_list:
                mod_list.append(frac)
                frac *= 10
                div = frac // denominator
                div_list.append(div)
                frac_num += 1
            else:
                not_the_same = False
                repeat_start = mod_list.index(frac)
        ret = ""
        if neg:
            ret += "-"
        ret += str(int_part)
        if is_int:
            return ret
        ret += "."
        if not not_the_same:
            for i in range(0,repeat_start):
                ret += str(div_list[i])
            ret += "("
            for i in range(repeat_start,len(div_list)):
                ret += str(div_list[i])
            ret += ")"
        else:
            for i in div_list:
                ret += str(i)
        return ret


u = Solution()
print(u.fractionToDecimal(1, 6))
