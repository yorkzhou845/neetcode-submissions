class Solution:
    def getSum(self, a: int, b: int) -> int:
        #a ^ b is the add
        #a & b is the carry bits
        mask = 0xFFFFFFFF#32 bit of 1s

        #create the 32 bit representations
        a &= mask
        b &= mask

        carry = a&b
        sig = a^b
        while carry:
            carry = (carry << 1) & mask#shift the bits to add, always apply mask
            sig2 = sig ^ carry
            carry &= sig
            sig = sig2
        #Python does not automatically interpret a positive integer as negative based on its 32nd bit.
        if sig <= 0x7FFFFFFF: return sig#0111.... so positive
        else:
            return sig - (1<<32)#similar to how 5 becomes -5 by subtracting 10

        