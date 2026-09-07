class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        hashmap = {}
        for i in s:
            if hashmap.get(i) == None:
                hashmap[i] = 0
            else:
                hashmap[i] += 1

        hashmap2 = {}
        for j in t:
            if hashmap2.get(j) == None:
                hashmap2[j] = 0
            else:
                hashmap2[j] += 1

        return hashmap == hashmap2

