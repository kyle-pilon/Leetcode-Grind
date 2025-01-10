class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashMap = collections.defaultdict(int)
        res = 0 

        for num in nums:
            if not hashMap[num]:
                hashMap[num] = hashMap[num - 1] + hashMap[num + 1] + 1
                hashMap[num - hashMap[num - 1]] = hashMap[num]
                hashMap[num + hashMap[num + 1]] = hashMap[num]
                res = max(res, hashMap[num])
        return res
            