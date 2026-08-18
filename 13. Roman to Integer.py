class Solution:
    def romanToInt(self, s: str) -> int:
        dd_i = [1, 4, 5, 9, 10, 40, 50,
                90, 100, 400, 500, 900, 1000]
        rr_i = ["I", "IV", "V", "IX", "X", "XL", "L",
                "XC", "C", "CD", "D", "CM", "M"]
        dd_rom = {i: k  for i, k in zip(rr_i, dd_i)}
        res = 0
        i = 0
    
        while i < len(s):
            if i == len(s) - 1:
                res += dd_rom[s[i]]
                i += 1
            else: 
                if s[i] + s[i+1] in rr_i:
                    res += dd_rom[s[i] + s[i+1]]
                    i += 2
                else:
                    res += dd_rom[s[i]]
                    i += 1

        return res
