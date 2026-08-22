class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p1 = 0
        p2 = len(numbers) - 1
        while p1 < len(numbers):
            if numbers[p1] + numbers[p2] == target: return [1 + p1, 1 + p2]
            elif numbers[p2] < target - numbers[p1]: p1 += 1#p2 stay at the same place since p1 is getting larger, p2 must be the same or slightly less to satisfy condition
            else: p2 -= 1

        
        

