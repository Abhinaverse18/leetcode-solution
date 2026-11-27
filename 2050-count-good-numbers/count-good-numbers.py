class Solution:
    MOD = 10**9 + 7

    def power(self, base: int, exp: int) -> int:
        if exp == 0:
            return 1

        half = self.power(base, exp // 2)
        result = half * half % self.MOD

        if exp & 1:
            result = result * base % self.MOD
        return result

    def countGoodNumbers(self, n: int) -> int:
        even_positions = (n + 1) // 2
        odd_positions = n // 2
        return self.power(5, even_positions) * self.power(4, odd_positions) % self.MOD