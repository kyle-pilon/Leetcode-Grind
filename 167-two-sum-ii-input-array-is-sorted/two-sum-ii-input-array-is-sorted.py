class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            total = numbers[left] + numbers[right]
            if total == target:
                return [left + 1, right + 1] # Add 1 to both indices because we want 1-indexed array
            if total > target:
                right -= 1
            if total < target:
                left += 1
        return