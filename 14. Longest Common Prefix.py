class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_str = min(strs, key=len)
        max_preffix = ""
        for i in range(1, len(min_str)+1):
            for string in strs:
                if min_str[:i] != string[:i]:
                    return max_preffix
            max_preffix = min_str[:i]
        return max_preffix
