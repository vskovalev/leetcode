class Solution:
    def intToRoman(self, num: int) -> str:
        dd_i = [1, 4, 5, 9, 10, 40, 50,
                90, 100, 400, 500, 900, 1000]
        rr_i = ["I", "IV", "V", "IX", "X", "XL", "L",
                "XC", "C", "CD", "D", "CM", "M"]
        res = ""
        nums = num

        for k in range(len(dd_i)-1,-1,-1):
            m = nums // dd_i[k]
            nums = nums - m*dd_i[k]
            res += m*rr_i[k]
        return res
