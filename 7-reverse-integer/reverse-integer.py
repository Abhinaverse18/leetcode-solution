class Solution:
    def reverse(self, x: int) -> int:

        sign = -1 if x < 0 else 1
        x = abs(x)


        reverse_n = 0
        while x > 0:
            last_digit = x %10
            reverse_n = (reverse_n * 10) + last_digit

            x = x // 10

        reverse_n = reverse_n * sign

        if reverse_n < -2**31 or reverse_n > 2**31 - 1:
            return 0

        return reverse_n


        