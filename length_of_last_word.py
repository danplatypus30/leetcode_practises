class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        curr = 0
        last = 0
        for i in range(len(s)):
            if s[i] != ' ':
                curr += 1
                last = curr
            else:
                curr = 0
        return last
