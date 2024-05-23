class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = 0
        max = nums[0] # max sum, start with first item
        for i in nums:
            sum = sum + i
            if sum < 0:
                sum = 0
            if sum != 0 and sum > max:
                max = sum
            elif sum == 0 and i > max:
                max = i
        return max
