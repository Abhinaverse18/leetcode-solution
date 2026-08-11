class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = {}
        for x in s1:
            s1_count[x] = s1_count.get(x , 0) + 1

        if len(s1) == 0:
            return True

        window_size = len(s1)
        if len(s2) < window_size:
            return False

        window_count = {}

        for i in range(window_size):
            x = s2[i]
            window_count[x] = window_count.get(x , 0) + 1
        if window_count == s1_count:
            return True

        for right in range(window_size , len(s2)):
            window_count[s2[right]] = window_count.get(s2[right] , 0) + 1

            left = right - window_size

            window_count[s2[left]] -= 1

            if window_count[s2[left]] == 0:

                del window_count[s2[left]]

            if window_count == s1_count:
                return True

        return False



        


        