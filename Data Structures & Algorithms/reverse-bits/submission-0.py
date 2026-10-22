class Solution:
    def reverseBits(self, n: int) -> int:
        #bit at i move to position index 31 - i
        res = 0
        for i in range(32):#0 to 31
            if (n >> i) & 1:#if the bit is not 0
                res ^= (1 << (31 - i))#put a 1 in that place
        
        return res

        