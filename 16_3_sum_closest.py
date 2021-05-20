import math
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)

        smallestDelta = math.pow(2, 31)
        closestSum = 0

        for i in range(0, len(nums)):
            j = i + 1
            k = len(nums) - 1
            while (j < k):
                threeSum = nums[i] + nums[j] + nums[k]
                if (threeSum == target):
                    return target
                delta = threeSum - target
                if (abs(delta) < abs(smallestDelta)):
                    smallestDelta = delta
                    closestSum = threeSum
                if (threeSum > target):
                    k -= 1
                else:
                    j += 1
        return closestSum
