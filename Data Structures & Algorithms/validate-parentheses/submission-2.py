class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match = {')':'(', '}':'{', ']':'['}

        for c in s:
            if c not in match:
                stack.append(c)
            elif match and stack and stack.pop() == match[c]:#they match
                continue
            else:
                return False
        
        if stack: return False
        else: return True

        