class Solution:
    def trap(self, height: List[int]) -> int:
        trappedWater: int = 0
        length: int = len(height) - 1

        firstIndex: int = 0
        lastIndex: int = length
        # we do this because we need to find the first index that represents a valid bar
        while (firstIndex < length and height[firstIndex] == 0):
            firstIndex += 1
        while (lastIndex >= 0 and height[lastIndex] == 0):
            lastIndex -= 1

        if (firstIndex == lastIndex):
            return 0

        i = firstIndex
        while (i < lastIndex):  # should it be lastIndex + 1?? check!
            increment = 0
            for j in range(i + 1, lastIndex + 1):  # should it be lastIndex ?? check!
                maxHeight = max(height[i+1:])
                if (height[i] > maxHeight):
                    height[i] = maxHeight
                # we want to find the first pair of (i, j) where height[j] >= height[i]
                if (height[i] > height[j]):  # and height[i] <= maxHeight
                    increment += 1
                    trappedWater += height[i] - height[j]
                else:
                    break
            i += increment + 1
        return trappedWater
