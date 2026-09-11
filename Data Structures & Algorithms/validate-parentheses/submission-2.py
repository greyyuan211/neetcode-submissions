class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {")": "(", "]": "[", "}": "{"}
        stack = []

        for c in s:
            if c in closeToOpen: #c is a closer
                if not stack or stack[-1] != closeToOpen[c]: # if stack is not empty or stack the pop is not matching
                    return False
                stack.pop()
            else:
                stack.append(c)
        return False if stack else True