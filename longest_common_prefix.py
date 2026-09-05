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
        


        