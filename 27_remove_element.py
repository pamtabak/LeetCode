class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        counter = 0
        index = 0
        originalLength = len(nums)
        while (counter < originalLength):
            counter += 1
            if (nums[index] == val):
                del nums[index]
                continue
            index += 1
        return len(nums)
