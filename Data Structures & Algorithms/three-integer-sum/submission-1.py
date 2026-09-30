class Solution:#p1, p2, p3 are picked in index order
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()#help prevent dups
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1#returns 0 if not available

        res = []
        for i in range(len(nums)):

            p1 = nums[i]#decrease the count
            counts[p1] -= 1#means that it is a potential candidate, prevent duplicate use
            #always decrement it 
            if i > 0 and nums[i] == nums[i-1]:#short circuiting
                continue
           

            for j in range(i + 1, len(nums)):
                p2 = nums[j]
                counts[p2] -= 1#decrement before because its a potential candidate. If it is a dupe, it doesnt matter


                if j > i + 1 and nums[j] == nums[j-1]:#skip duplicate p2 values
                    continue

                p3 = -(p2 + p1)#not exacttly a 3rd pointer
                if counts.get(p3, 0) > 0: #check for the other exists
                    res.append([p1, p2, p3])

            for j in range(i + 1, len(nums)): counts[nums[j]] += 1#need to restore counts

        return res