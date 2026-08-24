class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        count = {}
        nums.sort()  # sort so duplicates are adjacent

        # build frequency table
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        res = []

        for i in range(len(nums)):
            p1 = nums[i]

            # remove current i so it cannot be used as the third value
            count[p1] -= 1

            # skip duplicate p1 values
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, len(nums)):
                p2 = nums[j]

                # remove current j so count only represents values after j
                count[p2] -= 1

                # skip duplicate p2 values
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                target = -(p1 + p2)

                # if target still exists to the right of j,
                # then we found a valid triplet
                if target in count and count[target] >= 1:
                    res.append([p1, p2, target])

            # restore all j values before moving to the next i
            for j in range(i + 1, len(nums)):
                count[nums[j]] += 1

        return res