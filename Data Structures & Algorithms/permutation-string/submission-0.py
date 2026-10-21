class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target = 26 * [0]
        for c in s1: target[ord(c) - ord('a')] += 1#dictionaries cannot be keys easily. Use parenthesis
        test = 26 * [0]

        for i in range(0, len(s2) - len(s1) + 1):
            for j in range(i, i + len(s1)):
                test[ord(s2[j]) - ord('a')] += 1#j is an index
            if test == target: return True
            else: test = 26 * [0]

        
        return False



