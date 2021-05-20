class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # we first order the array
        nums = sorted(nums)
        result = []

        # since it is ordered, it is easier to search
        for i in range(0, len(nums)):
            if (nums[i] > 0):  # it means we already went through all the elements below 0
                continue
            j = i + 1
            k = len(nums) - 1
            while (j < k):
                res = nums[i] + nums[j] + nums[k]
                if (res == 0):
                    currentResult = [nums[i], nums[j], nums[k]]
                    if (currentResult not in result):
                        result.append(currentResult)
                    j += 1
                    k -= 1
                elif (res > 0):
                    k -= 1  # nums[k] is greater than nums[j]
                else:
                    j += 1
        return result
