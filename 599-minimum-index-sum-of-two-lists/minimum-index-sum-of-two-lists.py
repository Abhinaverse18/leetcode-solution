class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        mp = {}
        for i in range(len(list1)):
            mp[list1[i]] = i

        min_sum = float('inf')
        ans = []

        for j in range(len(list2)):
            if list2[j] in mp:
                total = mp[list2[j]] + j

                if total < min_sum:
                    min_sum = total
                    ans = [list2[j]]

                elif total == min_sum:
                    ans.append(list2[j])

        return ans