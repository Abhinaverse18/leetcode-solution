class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        n = len(s)
        left = 0
        right = 0
        ans = 0
        window = s[left : right]

        seen = set()
        for right in range(n):

            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])

            ans = max(ans , right - left + 1)


        return ans




        