class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        l = len(digits)
        c = 0
        for i in range(l):
            m = l - i - 1
            if digits[m] == 9:
                c = 1
                digits[m] = 0
            else:
                digits[m] += 1
                c = 0
                break
        if c == 1:
            digits.insert(0, 1)
        return digits