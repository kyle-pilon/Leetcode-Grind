class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # This problem was silly, had to re-write the hashSet implementation for the final test case
        # Exceeding time limit
        hashMap = collections.defaultdict(int)
        res = 0 

        for num in nums:
            if not hashMap[num]:
                hashMap[num] = hashMap[num - 1] + hashMap[num + 1] + 1
                hashMap[num - hashMap[num - 1]] = hashMap[num]
                hashMap[num + hashMap[num + 1]] = hashMap[num]
                res = max(res, hashMap[num])
        return res
            