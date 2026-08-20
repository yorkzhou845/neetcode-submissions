class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        prefix = 1#stores the accumlated product from before
        for i in range(len(nums)):
            result[i] *= prefix#only does the stuff from before. Need to multiple and cannot set to 0 just in prefix is 0
            prefix *= nums[i]
        
        suffix = 1
        for i in range(len(nums) - 1, -1, -1):#2nd bound is awlays excsluvie so need to go to -1
            result[i] *= suffix
            suffix *= nums[i]

        return result