class Solution:
    def myAtoi(self, s: str) -> int:
        k = 0
        s = s.lstrip()

        if len(s) == 0:
            return 0

        if s[0] == '-':
            sign = -1
            s = s[1:]
        elif s[0] == '+':
            sign = 1
            s = s[1:]
        else:
            sign = 1

        for i in s:
            if i.isdigit():
                k = k * 10 + int(i)
            else:
                break
        
        if k >= 2**31 and sign == -1:
            return 2**31*sign
        elif k >= 2**31 - 1 and sign == 1:
            return 2**31 - 1
        else:
            return k*sign
