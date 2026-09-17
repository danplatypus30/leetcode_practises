class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        j = 0
        i = 0
        while i < len(haystack):
            while haystack[i + j] == needle[j]:
                j = j + 1
                if j >= len(needle) or i + j >= len(haystack):
                    break
            if j >= len(needle) or i + j >= len(haystack):
                break
            else:
                j = 0
            i = i + 1
            # print("i is", i, "j is", j, "k is", k)
        if j >= len(needle):
            return i
        return -1