class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        if strs[0] == "":
            return ""
        curr = strs[0][0]
        index = 0
        char = 0
        while curr is not None:
            if index == len(strs):
                # if looped through list, move to next char
                prefix += curr
                index = 0
                char += 1
                if char > (len(strs[index]) - 1):
                    break
                curr = strs[index][char]

            if char > (len(strs[index]) - 1):
                break

            if strs[index][char] != curr:
                break
            # if ==, common prefix, continue checking
            
            print(strs[index][char])
            # increment
            index += 1

        return prefix
        

# faster solution
class Solution:
    def longestCommonPrefix2(self, strs: List[str]) -> str:
        ans = ""
        # sort lexicographically
        # flavour
        # flow
        # flower

        # apple
        # banana
        # curry

        strs = sorted(strs)
        # just care about first and last since sorted
        first = strs[0]
        # last index is arraylen -1
        last = strs[-1]
        # if strs = [""], len(first) and len(last) = 0
        # skip for loop
        # output ans gracefully
        # lesser of lengths of first, last
        for i in range(min(len(first), len(last))):
            # if char not match, return 
            if (first[i] != last[i]):
                return ans
            # if match, add to ans
            ans += first[i]

        return ans
        
        


        
        