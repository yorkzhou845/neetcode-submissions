class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        table = {}
        for num in nums:
            if num in table: table[num] += 1
            else: table[num] = 1
        
        descending = sorted(table.items(), key = lambda key: key[1], reverse = True)#use the keys to sort in descending order
        return [descending[i][0] for i in range(k)]#do not need the entire tuple, just the vals
        