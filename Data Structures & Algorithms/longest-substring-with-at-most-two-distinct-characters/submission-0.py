class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        l = 0
        r = 0
        output = 0
        
        frequency = defaultdict(int)
        for r in range(len(s)):
            frequency[s[r]] += 1
            while len(frequency) > 2:
                frequency[s[l]] -= 1

                if frequency[s[l]] == 0:
                    frequency.pop(s[l])
                l += 1
            output = max(output, r - l + 1)
        return output
        