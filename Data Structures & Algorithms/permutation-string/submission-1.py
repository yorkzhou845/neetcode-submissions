class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:#do not need to rebuild target evertime. Just remove counts of the first character and tack on the last
        if len(s1) > len(s2): return False

        target = 26 * [0]
        test = 26 * [0]

        for i in range(len(s1)): 
            target[ord(s1[i]) - ord('a')] += 1#dictionaries cannot be keys easily. Use parenthesis
            test[ord(s2[i]) - ord('a')] += 1
        
        if test == target: return True#done with base case
        
        for i in range(len(s1), len(s2)):#the pointer is the end of the window for this solution
            test[ord(s2[i - len(s1)]) - ord('a')] -= 1#subtract 1 from the old starting char
            test[ord(s2[i]) - ord('a')] += 1#add the last charater. Everything else between should stay the same
            if test == target: return True
        
        return False



