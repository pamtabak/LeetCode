class Solution:
    def countAndSay(self, n: int) -> str:
        if (n == 1):
            return "1"
        res = self.countAndSay(n-1)
        newRes = ""
        lastChar = res[0]
        count = 1
        for char in range(1, len(res)):
            if (res[char] == lastChar):
                count += 1
            else:
                newRes += str(count) + str(lastChar)
                count = 1
                lastChar = res[char]
        newRes += str(count) + str(lastChar)
        return newRes
