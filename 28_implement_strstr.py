class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if (not needle):
            return 0
        if (not haystack or len(needle) > len(haystack)):
            return -1
        i = 0
        j = 0
        found = 0
        while (i < len(haystack) and j < len(needle)):
            if (haystack[i] != needle[j]):
                i += 1
                if (found != 0):
                    i -= found
                found = 0
                j = 0
                continue
            j += 1
            i += 1
            found += 1
            if (found == len(needle)):
                return (i-j)
        return -1

