class Solution:#DICTIONARIES ARE UNHASHABLE SO CANNOT BE KEYS
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}#{(()):[]} tuples followed by list of strings
        curr = {}#current hashtable associated with current string. O(1) because at max 26 characters
        for s in strs:#O(n+m)
            for c in s:
                if c in curr: curr[c] += 1
                else: curr[c] = 1

            new = tuple(sorted(curr.items()))#need to convery hastable to ordered tuple so can use as key
            if new in seen: seen[new].append(s)#if the hastable has already been added, then add the current string to the list of strings
            else: seen[new] = [s]#
            curr.clear()#need to reset
        
        return list(seen.values())
