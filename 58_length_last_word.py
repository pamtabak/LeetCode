class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split(' ')
        for i in range(len(words) - 1, -1, -1):
            word = words[i].strip()
            if (word):
                return len(word)
        return 0
