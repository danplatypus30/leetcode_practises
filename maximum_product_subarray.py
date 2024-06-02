class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        product = 1
        max = nums[0]
        for i in nums:
            product *= i
            if product > max:
                max = product
            if product == 0:
                product = 1
        product = 1
        for j in reversed(range(len(nums))):
            product *= nums[j]
            if product > max:
                max = product
            if product == 0:
                product = 1
        return max
