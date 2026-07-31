class Solution:
    def minimumPushes(self, word: str) -> int:
        ww = len(word) // 8

        ww = sum([i * 8 for i in range(1, ww+1)]) + (ww+1)*(len(word) % 8)

        return ww
