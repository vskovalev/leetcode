class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        mm = len(needle)
        for i in range(0, len(haystack)-mm+1):
            if haystack[i:i+mm] == needle:
                return i
        return -1
