class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # radix sort 26 char
        ans = [0] * len(strs)
        arr = []
        rad = [0] * 26
        max_a = 1
        for a in strs[0]:
            rad[ord(a)-ord('a')] += 1
        arr.append(rad)
        for i in range(1, len(strs)):
            # check if in arr
            exists = False
            rad_t = [0] * 26
            for c in strs[i]:
                rad_t[ord(c)-ord('a')] += 1
            for e in range(len(arr)): #rad arr of 26
                all_equal = True
                for b in range(26):
                    if arr[e][b] != rad_t[b]:
                        all_equal = False
                        break
                if all_equal == True:
                    exists = True
                    ans[i] = e
                    break
            if exists == False:
                arr.append(rad_t)
                ans[i] = len(arr) - 1
                max_a += 1
        final_ans = []
        for x in range(max_a):
            final_ans.append([])
        for i in range(len(ans)):
            final_ans[ans[i]].append(strs[i])
        return final_ans
                
                
            
        