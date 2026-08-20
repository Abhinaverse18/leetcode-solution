class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:

        count = {}

        for a in nums1:
            for b in nums2:
                total = a + b

                if total in count:
                    count[total] += 1

                else:
                    count[total] = 1
        ans = 0

        for c in nums3:
            for d in nums4:
                total = c + d

                if -total in count:
                    ans += count[-total]

        return ans
                    

            
        