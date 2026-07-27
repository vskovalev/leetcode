# 6. Zigzag Conversion
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"

# Write the code that will take a string and make this conversion given a number of rows:

# string convert(string s, int numRows);
 

# Example 1:

# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
# Example 2:

# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# P     I    N
# A   L S  I G
# Y A   H R
# P     I
# Example 3:

# Input: s = "A", numRows = 1
# Output: "A"
 

# Constraints:

# 1 <= s.length <= 1000
# s consists of English letters (lower-case and upper-case), ',' and '.'.
# 1 <= numRows <= 1000

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if (numRows == 1) or (numRows == len(s)):
            return s
        elif (numRows == 2):
            return s[0::2] + s[1::2] 
        else:
            it = 0
            len_zigzag = 0
            lines = []
            len_connect_zigzag = numRows - 2
            result = ""

            while it < len(s):
                len_zigzag += 1
                if len_zigzag % 2 == 1:
                    num_zigzag_connection = len_zigzag // 2
                    num_zigzag_strokes = (len_zigzag // 2) + 1
                    start = (num_zigzag_strokes - 1) * numRows + \
                            num_zigzag_connection * len_connect_zigzag
                    end = num_zigzag_strokes * numRows + \
                            num_zigzag_connection * len_connect_zigzag
                    lines.append(s[start:end:].ljust(numRows))
                    it += numRows
                else: 
                    num_zigzag_connection = len_zigzag // 2
                    num_zigzag_strokes = len_zigzag // 2

                    start = numRows * num_zigzag_strokes + \
                            (num_zigzag_connection - 1) * len_connect_zigzag
                    end = numRows * num_zigzag_strokes + \
                            num_zigzag_connection * len_connect_zigzag
                    lines.append((" " + s[start:end:][::-1] + " ").rjust(numRows))
                    it += len_connect_zigzag

            return "".join(
                    line[row]
                    for row in range(numRows)
                    for line in lines
                    if line[row] != " "
                )
