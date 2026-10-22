class Solution:
    def hammingWeight(self, n: int) -> int:
        total = 0
        for i in range(32):
            mask = 1 << i#put a 1 in the place you are trying to check. Mask is all 0s except the highest place
            compare = mask & n#compare the place with the actually value in n
            if compare == mask:#if the compare is 
                total += 1
        
        return total


