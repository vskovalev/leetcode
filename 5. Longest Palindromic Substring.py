# Given a string s, return the longest palindromic substring in s.

 

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:

# Input: s = "cbbd"
# Output: "bb"
 

# Constraints:

# 1 <= s.length <= 1000
# s consist of only digits and English letters.

class Solution:
    def longestPalindrome(self, s: str) -> str:
        i = 0
        str_max_palindrom = ''
        len_max_palindrom = 0
        
        if len(s) == 1: 
            return s

        while True: 
            for j in range(i+1, len(s)+1):
                part_s = s[i:j]

                if ((part_s[::-1] == part_s) and 
                    (j-i > len_max_palindrom)):

                    str_max_palindrom = part_s
                    len_max_palindrom = j-i
                    
            i += 1 

            if i == len(s):
                break

        return str_max_palindrom
