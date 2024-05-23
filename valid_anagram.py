class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # radix sort
        letters = [0] * 26
        for i in s:
            int_letter = ord(i) - 97 # a is 97 in dec
            letters[int_letter] += 1
        
        for j in t:
            int_letter2 = ord(j) - 97
            letters[int_letter2] -= 1
        
        all_zero = True
        for k in letters:
            if k != 0:
                all_zero = False
        return all_zero
            