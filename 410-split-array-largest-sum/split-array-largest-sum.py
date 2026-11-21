class Solution:
    def countstudent(self, nums: List[int], pages: int) -> int:
        student = 1
        pages_student = 0
        for num in nums:
            if pages_student + num <= pages:
                pages_student += num
            else:
                student += 1
                pages_student = num
        return student

    def findpages(self, nums: List[int], n: int, m: int) -> int:
        if m > n:
            return -1
        low = max(nums)
        high = sum(nums)

        while low <= high:
            mid = (low + high) // 2
            students = self.countstudent(nums, mid)
            if students > m:
                low = mid + 1
            else:
                high = mid - 1
        return low

    def splitArray(self, nums: List[int], k: int) -> int:
        return self.findpages(nums, len(nums), k)