class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        ans = []
        p_count = {}
        
        for ch in p:
            p_count[ch] = p_count.get(ch , 0) + 1

        window_size = len(p)

        left = 0
        right = 0
        window  = {}
        while right < len(s):

            ch = s[right]
            window[ch] = window.get(ch , 0) + 1
            
            if right - left + 1 == window_size:

                if window  == p_count:
                    ans.append(left)

                left_ch = s[left]
                window[left_ch] -= 1

                if window[left_ch] == 0:
                    del window[left_ch]

                left += 1

            right += 1


        return ans

                




        