class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        waste = len(nums)
        i = 0
        while i < waste:
            if nums[i] == val:
                # swap
                nums[i] = nums[waste-1]
                waste = waste - 1
                # check new i
                # no need to replace last index
            else:
                i = i + 1
            #print(nums)
            #print("i is", i)
        return i

