class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(len(nums)-1):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            ni = nums[i]
            j = i + 1
            nj = nums[j]
            k = len(nums) - 1
            nk = nums[k]
            while(j < k):
                sum = ni + nj + nk
                if sum > 0:
                    k -= 1
                    nk = nums[k]
                elif sum < 0:
                    j += 1
                    nj = nums[j]
                elif sum == 0:
                    ans.append([ni,nj,nk])
                    j += 1
                    nj = nums[j]
                    while nj == nums[j-1] and j < k:
                        j += 1 # skip duplicates
                        nj = nums[j]
        return ans