class Solution:
    def minWindow(self, s: str, t: str) -> str:

        need = {}
        for ch in t:
            need[ch] = need.get(ch , 0) + 1

        window = {}
        have  = 0
        left = 0
        ans = ""
        ans_len = float('inf')

        for right in range(len(s)):
            ch = s[right]

            if ch in need:
                window[ch] = window.get(ch , 0) + 1
                if window[ch] == need[ch]:
                    have += 1

            while have == len(need):
                if right - left + 1 < ans_len :
                    ans_len = right - left + 1
                    ans = s[left : right + 1]
                left_char = s[left]

                if left_char in need:
                    window[left_char] -= 1
                    if window[left_char] < need[left_char]:
                        have -= 1

                left += 1

        return ans
                
         