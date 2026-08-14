class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        def atmost(k):

            if k < 0:
                return 0

            left = 0
            ans = 0
            current_sum = 0

            for right in range(len(nums)):
                current_sum += nums[right]

                while current_sum > k:
                    current_sum -= nums[left]
                    left += 1

                ans += right - left + 1

            return ans

        return atmost(goal) - atmost(goal - 1)