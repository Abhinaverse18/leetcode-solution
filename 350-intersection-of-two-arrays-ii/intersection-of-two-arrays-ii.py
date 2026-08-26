class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        count = {}
        ans = []

        for x in nums1:
            if x in count:
                count[x] += 1

            else:
                count[x] = 1

        for x in nums2:
            if x in count and count[x] > 0:
                ans.append(x)

                count[x] -= 1

        return ans
                

        