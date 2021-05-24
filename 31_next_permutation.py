class Solution:
    def reverse(self, nums: List[int], reverseFrom: int) -> None:
        i = reverseFrom
        j = len(nums) - 1
        while (i < j):
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp
            i += 1
            j -= 1

    def nextPermutation(self, nums: List[int]) -> None:
        i = len(nums) - 1
        found = False
        while (i > 0 and not found):
            if (nums[i] > nums[i-1]):
                found = True
                # we found the position where we want to make the swap
                # we need to check which one we will swap
                bestNum = 101  # since we know that the largest number in the list is 100
                bestNumPosition = i
                for j in range(i, len(nums)):
                    if (nums[j] > nums[i-1] and nums[j] <= bestNum):
                        bestNum = nums[j]
                        bestNumPosition = j
                tmp = nums[i-1]
                nums[i-1] = nums[bestNumPosition]
                nums[bestNumPosition] = tmp

                self.reverse(nums, i)
            else:
                i -= 1
        if (not found):
            self.reverse(nums, 0)
