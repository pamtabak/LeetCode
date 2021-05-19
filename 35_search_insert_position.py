class Solution:
    def binarySearch(self, nums: List[int], target: int, right: int, left: int) -> int:
        mid = int((right + left)/2)
        if (right <= left):
            # not found (we need to return with the closest answer)
            number = 0
            if (right < 0):
                return 0
            elif (right >= len(nums)):
                return len(nums)
            else:
                if (target > nums[right]):
                    right += 1
                return right

        if (nums[mid] == target):
            return mid
        if (target > nums[mid]):
            return self.binarySearch(nums, target, right, mid + 1)
        else:
            return self.binarySearch(nums, target, mid - 1, left)

    def searchInsert(self, nums: List[int], target: int) -> int:
        return self.binarySearch(nums, target, len(nums), 0)
