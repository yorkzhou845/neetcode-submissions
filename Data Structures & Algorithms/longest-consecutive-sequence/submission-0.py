class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:#once no longer +1 pattern, there can not be a longer consecutive stirng after that number
        if not nums: return 0#empty list
        seen = {}#hashtable holds number:True/False. True/False not accessed but need hashtable 
        for num in nums:
            if num not in seen: seen[num] = True#value isnt going to be used
        
        longest_len = 1
        curr_len = 1#always at least 1
        for key, val in seen.items():#hash table has good random key access
            temp_key = key + 1#start from 1 below becasue addition occurs first in the while loop before and the length is always at least 1
            if key - 1 not in seen:#this is the beginning
                while temp_key in seen:#the beginning and look foward
                    temp_key += 1#keep decrementing 
                    curr_len += 1
                if curr_len > longest_len: longest_len = curr_len
                curr_len = 1#reset it

        return longest_len
        