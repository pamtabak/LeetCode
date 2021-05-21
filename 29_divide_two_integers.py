class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        result = 0
        isNegative = False
        if ((dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0)):
            isNegative = True
        # checking for overflow
        if (dividend == -2147483648 and divisor == -1):
            return 2147483647
        dividend = abs(dividend)
        divisor = abs(divisor)
        multipliers = {1: divisor}
        multipliersKeys = [1]
        originalDividend = dividend
        while (dividend > 0):
            if (dividend >= divisor):
                result += 1
                for i in multipliersKeys:
                    if (i in multipliers and dividend >= multipliers[i]):
                        result += i - 1
                        dividend -= multipliers[i]
                        multipliers[result] = originalDividend - dividend
                        multipliersKeys = [result] + multipliersKeys
                        break
            else:
                dividend = 0

        if (isNegative):
            result = -1 * result
        return result
