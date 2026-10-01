class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if not heights: return 0

        p1 = 0
        p2 = len(heights) - 1
        max = 0

        while p1 < p2:
            shorter = min(heights[p1], heights[p2])
            area = shorter * (p2 - p1)
            if area > max: max = area

            if heights[p1] == shorter: p1 += 1#only move the shorter one in because for the same distance, if you want to increase, the taller must stay put
            else: p2 -= 1

        return max