class Solution:
    def reverseParentheses(self, s: str) -> str:
        a = [] # pos of (
        l = len(s)
        i = 0
        while i < l:
            #print(s[i], s)
            if s[i] == "(":
                a.append(i)
                s = s[:i] + s[i+1:]
                l -= 1
            elif s[i] == ")":
                #print(s[i],s)
                start = a.pop()
                inner = s[start:i]
                rev = inner[::-1]
                s = s[:start] + rev + s[i:]
                s = s[:i] + s[i+1:]
                l -= 1
            else:
                i += 1
        return s