class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            # ( ) is 40,41 { } is 123, 125 [ ] is 91, 93
            a = ord(i)
            if a == 40 or a == 123 or a == 91:
                stack.append(a)
            elif stack: # implied that a == 41 or a == 125 or a == 93
                # if stack not empty, pop
                b = stack.pop()
                if (a == 41 and b != 40) or (a == 125 and b != 123) or (a == 93 and b != 91):
                    return False
            else:
                # if stack empty, dont pop
                # stack should not be empty if input is not 40,123,91, means start with closing braces, immediately false
                return False
        if not stack:
            return True
        return False
        