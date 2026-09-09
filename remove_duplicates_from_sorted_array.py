class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        waste = len(nums)
        j = 1
        while j < waste:
            # check if duplicate
            if nums[j-1] == nums[j]:
                # swap to the back
                x = nums.pop(j)
                nums.append(x)
                waste = waste - 1
            else:
                j = j + 1
            #print(nums)
            #print("j is", j, "and waste is", waste)
        return j