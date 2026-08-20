class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash1 = {}#at most 26 characters (key value pairs)
        hash2 = {}
        for c in s:
            if c in hash1:
                hash1[c] += 1
            else:
                hash1[c] = 1
        
        for c in t:
            if c in hash2:
                hash2[c] += 1
            else:
                hash2[c] = 1
        
        return hash1 == hash2
        

        