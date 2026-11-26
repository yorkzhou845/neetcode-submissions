class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #dynamic programming
        #move from the back. The highest temperature time i
        #if the curr is < next -> res = 1
        #if the curr is > next -> res = res from next + 1, keep following
        res = [0] * len(temperatures)#holds delta, not the index
        temp_len = len(temperatures)
        for i in range(len(temperatures) - 1, -1, -1):
            val = temperatures[i]
            if i == temp_len - 1: continue
            next_highest = i+1#tracks index
            while val >= temperatures[next_highest]:#need to cpmare against temprature
                next_highest_val = res[next_highest]
                if next_highest_val == 0: break
                next_highest += res[next_highest]#get the next index
            if val < temperatures[next_highest]: res[i] = next_highest - i
            else: res[i] = 0
        
        return res


        