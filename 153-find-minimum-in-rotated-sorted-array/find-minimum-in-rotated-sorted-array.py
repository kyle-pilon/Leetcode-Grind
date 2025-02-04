class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        res = nums[left]

        while left <= right:
            if nums[left] < nums[right]:
                res = min(res, nums[left]) # Edge case, not rotated
                break
            mid = (left + right) // 2
            res = min(res, nums[mid])
            if nums[mid] >= nums[left]: 
                # Mid is part of left sorted portion, search right
                left = mid + 1
            else: 
                # Search left
                right = mid - 1
        return res
            