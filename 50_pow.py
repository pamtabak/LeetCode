class Solution:
    def myPow(self, x: float, n: int) -> float:
        if (n < 0):
            x = 1.0/x
        if (n == 0):
            return 1.0
        result = x
        iterationsLeft = abs(n) - 1
        currentIterations = 1
        calculated = {1: x}
        while (iterationsLeft != 0):
            calculatedKeys = sorted(calculated)
            for i in range(len(calculatedKeys) - 1, -1, -1):
                if (iterationsLeft >= calculatedKeys[i]):
                    currentIterations += calculatedKeys[i]
                    result *= calculated[calculatedKeys[i]]
                    iterationsLeft -= calculatedKeys[i]
                    calculated[currentIterations] = result
                    break
        return result
