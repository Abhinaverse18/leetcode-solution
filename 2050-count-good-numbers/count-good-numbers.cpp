class Solution {
    static constexpr long long MOD = 1'000'000'007;

    long long power(long long base, long long exp) {
        if (exp == 0) return 1;

        long long half = power(base, exp / 2);
        long long result = half * half % MOD;

        if (exp & 1) result = result * base % MOD;
        return result;
    }

public:
    int countGoodNumbers(long long n) {
        long long evenPositions = (n + 1) / 2;
        long long oddPositions = n / 2;
        return power(5, evenPositions) * power(4, oddPositions) % MOD;
    }
};