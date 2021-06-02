class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for word in strs:
            sortedWord = "". join(sorted(word)) 
            if (sortedWord not in anagrams):
                anagrams[sortedWord] = []
            anagrams[sortedWord].append(word)
        
        return list(anagrams.values())
