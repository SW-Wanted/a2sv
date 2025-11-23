class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_count = {}
        # print(char_count)
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
            # print(char_count)

        for index, char in enumerate(s):
            # print(f'index: {index}, char: {char} -> count: {char_count[char]}')
            if char_count[char] == 1:
                return index

        return -1
# Mandatory
