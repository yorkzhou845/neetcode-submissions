class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = 0
        total = 0
        while right < len(height) - 1:
            for i in range(right, len(height)):#search until find height[i] > height[left] or the greatest on the right side
                if height[i] >= height[left]:#the moment find something binger, stop
                    right = i
                    break
                elif height[i] > height[right]: right = i#important if there is nothing greater on the right anymore

            small = min(height[left], height[right])#have to use the min of the left and right side for no overflow. Even if the right side has nothing larger than the current, still works
            for i in range(left + 1, right):#iterate through adding on the difference in height. boundaries cannot hold water so must be exclusive on both ends
                total += small - height[i]

            left = right#put everything to the end
            right += 1#need to push the new_max one over or else may be stuck on the same peak

        return total

        
                

