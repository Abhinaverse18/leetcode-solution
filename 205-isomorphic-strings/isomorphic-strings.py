class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        s_to_t = {}
        t_to_s = {}

        i = 0
        while i < len(s):

            if s[i] in s_to_t :
                if s_to_t[s[i]] != t[i]:
                    return False

            if t[i] in t_to_s:
                if t_to_s[t[i]] != s[i]:
                    return False

            s_to_t[s[i]] = t[i]
            t_to_s[t[i]] = s[i]

            i += 1

        return True
        