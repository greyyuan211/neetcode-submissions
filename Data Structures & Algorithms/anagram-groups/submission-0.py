class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list) # {[0,0,0,...]:[eat,tea]}
        for s in strs:
            frequency = [0] * 26 # an array with 26 zeros
            for c in s:
                frequency[ord(c)-ord("a")] += 1 # increment the right position of the array
            result[tuple(frequency)].append(s) # add the frequency array as key, and append the str as value

        return (list(result.values()))