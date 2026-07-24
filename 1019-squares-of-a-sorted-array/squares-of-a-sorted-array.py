class Solution:
    def sortedSquares(self, nums):
        left = 0
        right = len(nums) - 1
        ans = [0] * len(nums)
        k = len(nums) - 1

        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                ans[k] = nums[left] * nums[left]
                left += 1

            else:
                ans[k] = nums[right] * nums[right]
                right -= 1

            k -= 1
        return ans 



 