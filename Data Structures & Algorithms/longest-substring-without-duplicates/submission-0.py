class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = ""#serves has hashtable and current length
        max_length = 0

        for i, char in enumerate(s):
            if char in sub: #already seen so done
                index = sub.index(char) #index of the dup
                sub = sub[index + 1:]#continue from after the last dup
            
            sub += char
            if len(sub) > max_length: max_length =  len(sub) #need to update on every iteration, not only when dups are found or else unique strings will return nothiong

        return max_length

