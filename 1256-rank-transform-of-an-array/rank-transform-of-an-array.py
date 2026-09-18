class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:

        sorted_arr = sorted(arr)

        rank = {}
        rank_num = 1

        for num in sorted_arr:

            if num not in rank:

                rank[num] = rank_num

                rank_num += 1

        for i in range(len(arr)):

            arr[i] = rank[arr[i]]

        return arr

        