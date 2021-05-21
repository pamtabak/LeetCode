class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # we first order the array
        nums = sorted(nums)
        result = []

        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                k = j + 1
                l = len(nums) - 1
                while (k < l):
                    res = nums[i] + nums[j] + nums[k] + nums[l]
                    if (res == target):
                        currentResult = [nums[i], nums[j], nums[k], nums[l]]
                        if (currentResult not in result):
                            result.append(currentResult)
                        k += 1
                        l -= 1
                    elif (res > target):
                        l -= 1
                    else:
                        k += 1
        return result
