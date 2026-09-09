class Solution:

    def encode(self, strs: List[str]) -> str:
        res = [] # faster than string += operation
        for s in strs:
            res.append(str(len(s)))
            res.append("?")
            res.append(s)
        #print(''.join(res))
        return ''.join(res)

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while (i < len(s)):
            j = s.find('?', i)
            length = int(s[i:j])
            res.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length

        return res

