class Solution:
    def reverse(self, x: int) -> int:
        if ((int(str(abs(x))[::-1]) < 2147483648) \
            or (x == 2147483648)) and x != 0:
            if x>0:
                return int(str(x)[::-1])
            elif x<0:
                return -1*int(str(x*-1)[::-1])
        else:
            return 0
        
