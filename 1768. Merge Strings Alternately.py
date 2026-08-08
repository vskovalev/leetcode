class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        mm, kk = min(len(word1), len(word2)), len(word1) > len(word2)
        if kk:
            return ''.join([i + j for i, j in zip(word1, word2)]) + word1[mm:]
        return ''.join([j + i for i, j in zip(word2, word1)]) + word2[mm:]
