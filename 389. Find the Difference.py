class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for i, j in zip(''.join(sorted(t)), ''.join(sorted(s)) + "1"):
            if i != j: return i
