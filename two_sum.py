class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashset = {}
        
        # hash table
        for i in range(len(nums)):
            hashset[nums[i]] = i # key = nums[0], value = 0
        
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hashset and hashset[diff] != i: 
                # first condition ensures diff exists in hashset
                # second condition ensures no two duplicate numbers used
                return [i, hashset[diff]] # return index of the two numbers

        return [] # no solution
