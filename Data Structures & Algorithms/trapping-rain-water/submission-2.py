class Solution:#space O(1), time O(n)
    def trap(self, height: List[int]) -> int:
        p1 = 0
        p2 = len(height) - 1
        leftmax = height[p1]
        rightmax = height[p2]
        total = 0
        while p1 < p2:
            if height[p2] > height[p1]: #if the right  wall is taller than the left wall, can safely reel in p1 to the right
                if height[p1] < leftmax:#current value is still lower than the leftmax
                    total += leftmax - height[p1]
                else:#there is a new left max
                    leftmax = height[p1]
                p1 += 1
            else:#left wall is taller than the right wall, can safely bring in p2 to the left
                if height[p2] < rightmax:#current value is lower than the right max
                    total += rightmax - height[p2]
                else:#there is a new right max
                    rightmax = height[p2]
                p2 -= 1

        return total