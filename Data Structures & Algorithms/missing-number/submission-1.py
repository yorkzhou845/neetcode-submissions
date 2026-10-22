class Solution:#appearing twice strategy. Numbers in nums are not sorted in order. XOR is cumulative
    def missingNumber(self, nums: List[int]) -> int:
        res =  len(nums)#set it to n since the loop will not be able to reach n, since exclusive
        for i in range(len(nums)):#skip out on the n
            res ^= i 
            res ^= nums[i]#if both exist, then the X0R returns 0. Since only 1 exists, then the result would just be itself 
        return res
        