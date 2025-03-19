class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashSet = set()

        for number in nums:
            if number in hashSet:
                return True
            hashSet.add(number)
        return False