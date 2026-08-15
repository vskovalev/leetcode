class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digits_dict = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        
        res = digits_dict[digits[0]]

        if len(digits) > 1:
            for num in digits[1:]:
                mm = []
                for k in res:
                    for j in digits_dict[num]:
                        mm.append(k + j)
                res = mm
        return res
