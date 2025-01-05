class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # HashMap to count occurances
        freq = [[] for i in range(len(nums) + 1)] # Index : Count, List : #'s occuring at count
        res = [] # Result list

        # Count occurances with HashMap
        for number in nums:
            count[number] = 1 + count.get(number, 0)
        # Use HashMap to build the frequency array
        for number, count in count.items(): # Iterate over HashMap Key : Value pairs
            freq[count].append(number)

        # Iterate over the frequency array from len(freq) - 1 -> 0, (-1 in 3rd argument -> backwards)
        for i in range(len(freq) - 1, 0, -1):
            for number in freq[i]:
                res.append(number)
                if len(res) == k:
                    return res
        
