class Solution:
    def findMaxLength(self, nums: List[int]) -> int:

        seen = {0 : -1}
        balance = 0
        max_length = 0

        for i in range(len(nums)):

            if nums[i] == 0:
                balance -= 1

            else:
                balance += 1

            if balance in seen:
                length  = i - seen[balance]
                max_length = max(max_length, length)

            else:
                seen[balance] = i

        return max_length

            

        


        