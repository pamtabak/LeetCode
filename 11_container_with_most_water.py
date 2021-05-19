class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        length = len(height) - 1

        for i in range(0, len(height)):
            if ((height[i] * (len(height) - 1 - i)) < maxArea):
                # this means that we already found a better solution
                continue
            for j in range(length, i, -1):
                if ((height[i] * (j - i)) < maxArea):
                    break
                h = min(height[i], height[j])
                l = j - i
                area = h * l
                if (area > maxArea):
                    maxArea = area
                if (height[j] >= height[i]):
                    # we already used height[i] to get the max area using (j - i) length, so there is no point continuing. any height presented here will be either smaller than height[i] (and generate a smaller area) or higher than height[i] and we will use height[i]
                    break
                else:
                    # it means height[j] was used to calculate the area. since the length only decreases (its j - i), we dont need to see other "i's" for that same height because it will be smaller and so for the next iteration we will only check for this range
                    length -= 1
        return maxArea
