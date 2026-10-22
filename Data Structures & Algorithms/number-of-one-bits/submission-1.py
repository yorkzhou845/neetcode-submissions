class Solution:
    
    def hammingWeight(self, n: int) -> int:
        total = 0
        while n:
            if n & 1: total += 1

            n >>= 1#need n reassignemtn
        return total

        