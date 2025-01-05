class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = defaultdict(list)

        for string in strs:
            count = [0] * 26 # a - z

            for char in string:
                count[ord(char) - ord("a")] += 1 # ASCII z : 122 - a : 97 = count[25]

            hashMap[tuple(count)].append(string)

        return list(hashMap.values())