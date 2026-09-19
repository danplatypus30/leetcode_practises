class Solution: 
    def searchInsert(self, nums: list[int], target: int) -> int: 
        left = 0 
        right = len(nums) - 1 
        while left <= right: 
            mid = (right - left) // 2 + left 
            # divide and round down
            #print(mid)
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid + 1 
            else:
                right = mid - 1
        
        if left > mid:
            return left
        return mid
