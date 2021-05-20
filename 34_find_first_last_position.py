class Solution:
    def addaptedBinarySearch(self, nums: List[int], target: int, right: int, left: int, isLeft: bool) -> int:
        mid = (right + left)//2

        if (mid < len(nums) and nums[mid] == target):
            if (right <= left):
                return mid
            elif (isLeft):
                res = self.addaptedBinarySearch(
                    nums, target, mid - 1, left, isLeft)
                if (res == -1):
                    return mid
                return res
            else:
                res = self.addaptedBinarySearch(
                    nums, target, right, mid + 1, isLeft)
                if (res == -1):
                    return mid
                return res

        if (right <= left):
            # not found
            return -1

        if (target > nums[mid]):
            return self.addaptedBinarySearch(nums, target, right, mid + 1, isLeft)
        else:
            return self.addaptedBinarySearch(nums, target, mid - 1, left, isLeft)

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if (len(nums) == 0):
            return [-1, -1]
        # we basically want to call two binary searches: one that finds the most left target and one that finds the most right
        return [self.addaptedBinarySearch(nums, target, len(nums), 0, True),  self.addaptedBinarySearch(nums, target, len(nums), 0, False)]
