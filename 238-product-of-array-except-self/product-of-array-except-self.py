class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # O(1) requires only one output array 
        res = [1] * len(nums) # We need initial 1 for correct product at each index

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1): # Reverse array iteration
            res[i] = res[i] * postfix
            postfix *= nums[i]

        return res