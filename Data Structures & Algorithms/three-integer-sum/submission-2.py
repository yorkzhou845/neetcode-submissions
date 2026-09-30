class Solution:#numbers that sum together move inward
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()#in place
        res = []
        for i, p1 in enumerate(nums):
            if p1 > 0: break#sorted order so if already positive, cannot continue
            if i > 0 and nums[i] == nums[i-1]: continue#dup from a previous pass

            p2 = i + 1#1 after i. not actually aaccessing index
            p3 = len(nums) - 1 #last element
            while p2 < p3:
                total = p1 + nums[p2] + nums[p3]
                if total > 0:
                    p3 -= 1
                elif total < 0:
                    p2 += 1
                else: 
                    res.append([p1, nums[p2], nums[p3]])
                    p2 += 1
                    p3 -= 1
                #skipping dups only until find valid answer. Then you can skip (helps prevent out of bounds)
                    while p2 < p3 and nums[p2] == nums[p2 - 1]:
                        p2 += 1

                    while p2 < p3 and nums[p3] == nums[p3 + 1]:
                        p3 -= 1

        return res