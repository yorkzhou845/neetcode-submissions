class Solution:
    def reverse(self, x: int) -> int:
        MAX = 2**31 - 1
        MIN = -2**31
        max = MAX // 10#truncate the least digit
        max_last_digit = MAX % 10
        min = MIN // 10 + 1#floor works opposite for negative
        min_last_digit = MIN % -10
        res = 0
        while x:
            digit = x % 10 if x >= 0 else x % -10#gets the least sig bit
            x = (x - digit) // 10#shift left by 1 digit basically
            #need to guanrntee that can append(1-9) digit to end. Cant divide simply because negative works opposite
            if res > max or (res == max and digit > max_last_digit):#overflow
                return 0
            if res < min or (res == min and digit < min_last_digit):#underflow
                return 0
            res = res * 10 + digit
        
        return res

            


                  