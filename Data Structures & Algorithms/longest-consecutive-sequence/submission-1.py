class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = {}#hold the value: length
        max = 0
        for num in nums:
            if num not in seen:#if already seen then it would have already been handled
                len_left = seen[num - 1] if num - 1 in seen else 0#left is the length of the left side
                len_right = seen[num + 1] if num + 1 in seen else 0#right is the length of the right side

                len_total = len_left + 1 + len_right
                seen[num] = len_total#any new number can only extend or merge conseccutive sequence
                seen[num - len_left] = len_total#the boundary of the left side
                seen[num + len_right] = len_total

                if len_total > max: max = len_total
                
        return max
            

        