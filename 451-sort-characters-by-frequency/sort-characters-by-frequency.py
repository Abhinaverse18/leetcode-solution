class Solution:
    def frequencySort(self, s: str) -> str:

        freq = {}
        for ch in s:
            if ch in freq:
                freq[ch] += 1

            else:
                freq[ch] = 1

        sorted_char = sorted(freq , key=freq.get , reverse=True)
        ans = ""
        for ch in sorted_char:
            ans += ch*freq[ch]

        return ans
        