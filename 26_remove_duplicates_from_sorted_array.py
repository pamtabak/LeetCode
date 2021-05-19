class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if (len(nums) == 0):
            return 0
        counter = 1
        index = 1
        lastSeenInt = nums[0]
        originalLength = len(nums)
        while (counter < originalLength):
            counter += 1
            if (nums[index] == lastSeenInt):
                del nums[index]
                continue
            lastSeenInt = nums[index]
            index += 1
        return len(nums)
