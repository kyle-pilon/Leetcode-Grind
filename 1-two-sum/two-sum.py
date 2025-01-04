class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {} # number : index

        for i, number in enumerate(nums):
            difference = target - number
            if difference in hashMap:
                return [hashMap[difference], i]
            hashMap[number] = i
        return
            