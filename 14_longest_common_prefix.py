class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        commonPrefix = ""
        firstString = strs[0]
        if (not firstString):
            return ""
        if (len(strs) == 1):
            return firstString
        for i in range(0, len(firstString)):
            for s in range(1, len(strs)):
                if (not strs[s] or len(strs[s]) <= i):
                    return commonPrefix
                if (firstString[i] != strs[s][i]):
                    return commonPrefix
            commonPrefix += firstString[i]

        return commonPrefix
