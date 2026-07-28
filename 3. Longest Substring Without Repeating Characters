class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_pos: dict[str, int] = {}
        best = 0
        def dfs(right: int, left: int) -> None:
            nonlocal best
            if right == len(s):
                return
            ch = s[right]
            if ch in last_pos and last_pos[ch] >= left:
                left = last_pos[ch] + 1
            last_pos[ch] = right
            best = max(best, right - left + 1)
            dfs(right + 1, left)
        dfs(0, 0)
        return best
