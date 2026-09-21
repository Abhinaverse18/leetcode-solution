class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:

        ans = []

        total = 0

        for i in range(len(nums)):
            total = total + nums[i]

            ans.append(total)

        return ans



        