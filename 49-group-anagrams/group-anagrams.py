class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups = {}

        for word in strs:
            key = "".join(sorted(word))

            if key not in groups:

                groups[key] = []

            groups[key].append(word)

        ans = []

        for group in groups.values():

            ans.append(group)

        return ans




        