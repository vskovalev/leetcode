class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cc1 = {}
        cc2 = {}

        for c in s:
            cc1[c] = cc1.get(c, 0) + 1
        
        for c in t:
            cc2[c] = cc2.get(c, 0) + 1
        
        if cc1.keys() != cc2.keys():
            return False

        for k in cc1.keys():
            if cc1.get(k) != cc2.get(k, 0):
                return False
        return True
