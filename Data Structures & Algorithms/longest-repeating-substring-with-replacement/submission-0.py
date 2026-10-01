class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}#helps find the most frequent letter in a substring and the current window size
        maxf = 0 #max frequency letter
        res = 0
        for i in range(len(s)):
            freq[s[i]] = freq.get(s[i], 0) + 1#update this new letter
            maxf = max(maxf, freq[s[i]])#find the most frequent letter now
            curr_window = sum(freq.values())#window size also used to find where the left is

            if curr_window > k + maxf:#
                left = i - curr_window + 1
                c = s[left]#left pointer
                freq[s[left]] -= 1
                curr_window -= 1

            res = max(res, curr_window)

        return res






        




                

