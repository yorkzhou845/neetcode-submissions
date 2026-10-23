class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for num in nums:
            seen[num] = seen.get(num, 0) + 1
        
        freq = sorted(seen.items(), key = lambda x: x[1], reverse = True)
        return [freq[i][0] for i in range(k)]


        