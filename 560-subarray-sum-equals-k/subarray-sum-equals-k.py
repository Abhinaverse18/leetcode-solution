class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        count = {0:1}

        ans = 0
        current_sum  = 0

        for num in nums:
            current_sum += num

            if current_sum - k in count:
                ans += count[current_sum - k]

            count[current_sum] = count.get(current_sum  ,  0) + 1

        return ans

        