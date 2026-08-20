class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash1 = [0] * 26#serves as a hashtable bscially
        hash2 = [0] * 26
        for c in s:
            hash1[ord(c) - ord('a')] += 1
        
        for c in t:
            hash2[ord(c) - ord('a')] += 1
        
        return hash1 == hash2
        