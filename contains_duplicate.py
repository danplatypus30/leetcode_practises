class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False # no duplicates
        
# hash set solution
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set() # declare a python hashset
        for num in nums:
            if num in seen: # O(1) search time, because seen[key] = value if exist, else null
                return True
            seen.add(num) # if not in hashset, add to hashset
        return False 
    # O(n) time