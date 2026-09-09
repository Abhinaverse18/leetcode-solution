class Solution:
    def thirdMax(self, nums: List[int]) -> int:

        first = float('-inf')
        second = float('-inf')
        third = float('-inf')

        for num  in nums:
            if num == first or num == second or num == third:
                continue

            if num > first:
                third = second
                second = first
                first = num

            else:
                if num > second:
                    third = second
                    second = num

                else:
                    if num > third:
                        third = num

        if third == float('-inf'):
            return first

        else:
            return third

        