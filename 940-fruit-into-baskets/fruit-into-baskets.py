class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        left = 0
        fruit_count = {}
        ans = 0

        for right in range(len(fruits)):

            fruit_count[fruits[right]] = fruit_count.get(fruits[right] , 0) + 1

            while len(fruit_count) > 2:
                fruit_count[fruits[left]] -= 1

                if fruit_count[fruits[left]] == 0:
                    del fruit_count[fruits[left]]

                left += 1

            ans = max(ans , right - left + 1)

        return ans 
        