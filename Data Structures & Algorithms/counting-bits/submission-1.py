class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for number in range(n + 1):#need to include last number
            total = 0
            for i in range(32):#start from least to most sig
                mask = 1 << i
                if mask & number: total += 1

            res.append(total)
        return res    

        