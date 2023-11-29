class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        d = abs(dividend)
        dv = abs(divisor)
        output = 0

        while d >= dv:
            tmp = dv
            mul = 1
            while d >= tmp:
                d -= tmp
                output +=mul
                mul +=mul
                tmp +=tmp
        if(dividend <0 and divisor >=0) or(divisor<0 and dividend >=0):
            output = - output
        return min(2147483647, max(-2147483648, output))            