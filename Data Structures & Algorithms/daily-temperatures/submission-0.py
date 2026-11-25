class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)#
        stack = []#(index, temp). keeps track of days that are still waiting for a warmer temperature.
        for i, val in enumerate(temperatures):
            while stack and val > stack[-1][1]:
                index, temp = stack.pop()
                res[index] = i - index
            stack.append((i, val))        
        return res

        
