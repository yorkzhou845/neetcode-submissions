class Solution:
    def hammingWeight(self, n: int) -> int:
        #set bit means a bit of value 1
        total = 0
        while n:
            total += 1
            n &= (n-1)#this removes a set 1 every time
        
        return total

        