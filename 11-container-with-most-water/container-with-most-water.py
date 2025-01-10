class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        left, right = 0, len(height) - 1

        while left < right:
            y = min(height[left], height[right])
            x = right - left
            currWater = x * y
            res = max(res, currWater)
            if height[left] < height[right]:
                left += 1
            elif height[left] > height[right]:
                right -= 1
            else: 
                left += 1 # Just choose to move either pointer if the y's are equal
        return res