class Solution:
    def adaptedBinarySearch(self, nums: List[int], target: int, left: int, right: int) -> int:
        mid = (right + left) // 2

        if (mid < len(nums) and nums[mid] == target):
            return mid

        if (right <= left):
            return -1

        if (nums[mid] >= nums[left]):
            # so it is correctly order in [left:mid+1]
            if (nums[left] <= target < nums[mid]):
                return self.adaptedBinarySearch(nums, target, left, mid - 1)
            else:
                return self.adaptedBinarySearch(nums, target, mid + 1, right)
        else:
            if (nums[right] >= target > nums[mid]):
                return self.adaptedBinarySearch(nums, target, mid + 1, right)
            else:
                return self.adaptedBinarySearch(nums, target, left, mid - 1)

    def search(self, nums: List[int], target: int) -> int:
        return self.adaptedBinarySearch(nums, target, 0, len(nums)-1)
