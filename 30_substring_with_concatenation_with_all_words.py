class Solution:
    def countTotalCharOfWordsLeft(self, words: List[str]) -> int:
        total = 0
        for word in words:
            total += len(word)
        return total
    
    def largestWordOfWordsLeft(self, words: List[str]) -> int:
        total = math.pow(-2, 31)
        for word in words:
            if (len(word) > total):
                total = len(word)
        return total
    
    def isPrefix (self, words : List[str], currentString: str) -> bool:
        for word in words:
            if (currentString in word):
                return True
        return False
        
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        #we iterate s searching for any word from words
        #if we find any, delete from word and try to find the next
        results  = []
        
        lenWords = self.countTotalCharOfWordsLeft(words)
        for i in range(len(s)):
            currentWords = deepcopy(words)
            currentLenWords = deepcopy(lenWords)
            if (currentLenWords > len(s) - i):
                break
            currentString = ""
            firstIndex = -1
            for j in range(i, len(s)):
                if (currentLenWords > (len(s) + len(currentString) - j)):
                    break
                currentString += s[j]
                if (currentString in currentWords):
                    currentLenWords -= len(currentString)
                    del currentWords[currentWords.index(currentString)]
                    if (firstIndex == -1):
                        firstIndex = j + 1 - len(currentString)
                    currentString = ""
                    if (len(currentWords) == 0):
                        results.append(firstIndex)
                        break
                if (not self.isPrefix(currentWords, currentString)):
                    break
        return results
