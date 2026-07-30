class Solution:
    def isValid(self, s: str) -> bool:
        kk = []
        for i in s:
            if i == "{" or i == "[" or i == "(":
                kk.append(i)
            elif len(kk) == 0:
                return False 
            elif (i == "}" and kk[-1] == "{") \
            or (i == "]" and kk[-1] == "[") \
            or (i == ")" and kk[-1] == "("):
                kk.pop()
            else:
                return False

        if len(kk) == 0:
            return True
        else:
            return False
