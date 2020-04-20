"""
Given a 32-bit signed integer, reverse digits of an integer.

Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1].
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""

class Integer_Inverse:
    def reverse(self, x):
        out = 0
        sign = 0
        if x < 0:
            x *= -1
            sign = 1
        i = 1
        digits = len(str(x))
        while i <= digits:
            out += (x % 10) * 10 ** (digits - i)
            x //= 10
            i += 1
        if out > 2**31 -1:
            return 0
        elif sign == 1:
            out *= -1
            return out
        else:
            return out
x = 1234567899
solution = Integer_Inverse()
print(solution.reverse(x))
