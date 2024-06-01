class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            if target == nums[0]:
                return 0
            else:
                return -1
        low = 0
        high = len(nums)-1
        mid = int(len(nums)/2)
        if nums[low] > nums[high]:
            # rotated, find pivot index
            mid_r = mid+1
            t_low = low
            t_high = high
            pivot = 0
            if mid_r >= len(nums):
                pivot = low
                pivot_r = low + 1
            else:
                while nums[mid] < nums[mid_r]:
                    if nums[low] < nums[mid]: # pivot at right half
                        t_low = mid
                    else: # pivot at left half
                        t_high = mid
                    mid = int((t_high-t_low)/2) + t_low
                    mid_r = mid + 1
                # binary search from 0 to pivot, pivot + 1 to end
                pivot = mid
                pivot_r = mid + 1
            while low <= pivot:
                mid = int((pivot-low)/2) + low
                if target == nums[mid]:
                    return mid
                if target > nums[mid]:
                    # target at right side
                    low = mid+1
                else:
                    # target at left side
                    pivot = mid-1
            # if reached here, target not in low ~ pivot
            while pivot_r <= high:
                mid = int((high-pivot_r)/2) + pivot_r
                if target == nums[mid]:
                    return mid
                if target > nums[mid]:
                    # target at right side
                    pivot_r = mid+1
                else:
                    # target at left side
                    high = mid-1
            return -1
        else:
            # normal binary search            
            while low <= high:
                mid = int((high-low)/2) + low
                if target == nums[mid]:
                    return mid
                if target > nums[mid]:
                    # target at right side
                    low = mid+1
                else:
                    # target at left side
                    high = mid-1
            return -1
                
            
