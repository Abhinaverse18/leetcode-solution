class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        words = s.split()

        if len(pattern) != len(words):
            return False

        word_to_pattern = {}
        pattern_to_word ={}

        for i in range(len(pattern)):
            if pattern[i] in pattern_to_word:
                if pattern_to_word[pattern[i]] != words[i]:
                    return False

            if words[i] in word_to_pattern:
                if word_to_pattern[words[i]] != pattern[i]:
                    return False

            pattern_to_word[pattern[i]] = words[i]
            word_to_pattern[words[i]] = pattern[i]

        return True

            