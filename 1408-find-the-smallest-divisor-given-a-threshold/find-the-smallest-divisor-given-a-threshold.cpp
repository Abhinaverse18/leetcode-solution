class Solution {
public:
    int smallestDivisor(vector<int>& nums, int threshold) {
        int lo = 1;
        int hi = *max_element(nums.begin(), nums.end());

        while (lo < hi) {
            int mid = (lo + hi) / 2;
            int sum = 0;
            for (int n : nums) {
                sum += (n + mid - 1) / mid;
            }
            if (sum <= threshold) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        return lo;
    }
};