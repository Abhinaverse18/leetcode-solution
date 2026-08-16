class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:

        seen = set()
        ans = set()

        left = 0

        for right in range(len(s)):

            if right - left + 1 == 10:
                sequence = s[left : right + 1]

                if sequence in seen:
                    ans.add(sequence)

                else:
                    seen.add(sequence)

                left += 1

        return list(ans)




        