class Solution:#recursinon
    def countBits(self, n: int) -> List[int]:
        #1101
        
        if n <= 0: return [0]
        
        result = self.countBits(n-1)#list
        if not n%2:#even
            result.append(result[n//2])#10->1010 has same number of 1s as 101 self.countBits(n - 1)] + self.countBits(n - 1) 
        else:#odd
            result.append(result[n//2] + 1)#does in place

        return result
        