class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort() # O(nlogn)

        for i, firstVal in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]: # Skip duplicates 
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                total = firstVal + nums[left] + nums[right]
                if total > 0:
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    res.append([firstVal, nums[left], nums[right]])
                    left += 1 # Right or left could be moved interchangeably
                    while left < right and nums[left] == nums[left - 1]: # Again skip duplicates
                        left += 1
        return res