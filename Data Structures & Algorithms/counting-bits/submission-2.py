class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n + 1)#include 0

        for i in range(1, n + 1):
            num = i
            while num != 0:#woring on 1 number at a time 
                res[i] += 1
                num &= (num - 1)
            
        return res


        