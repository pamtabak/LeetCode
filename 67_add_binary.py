class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if (len(b) > len(a)):
            a = "0"*(len(b) - len(a)) + a
        else:
            b = "0"*(len(a) - len(b)) + b
        sumOne = False
        result = ""
        for i in range(len(a)-1, -1, -1):
            binSum = int(a[i]) + int(b[i])
            if (sumOne):
                binSum += 1
                sumOne = False
            result = str(binSum % 2) + result
            sumOne = binSum >= 2
        if (sumOne):
            result = "1" + result
        return result
