class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        ans = []

        for i in range(len(nums)):

            num = abs(nums[i]) 

            index = num - 1

            nums[index] = -abs(nums[index])

        for i in range(len(nums)):

            if nums[i] > 0:
                ans.append(i + 1)

        return ans




        