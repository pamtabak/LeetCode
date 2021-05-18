class Solution:
    # this is the simplest solution, O(n**2) time complexity
    def basic_solution(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                if (nums[i] + nums[j] == target):
                    return [i, j]

    # this has O(n) time complexity and O(n) space complexity
    def map_solution(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for i in range(0, len(nums)):
            if (nums[i] not in nums_dict):
                nums_dict[nums[i]] = []
            nums_dict[nums[i]].append(i)

        for i in range(0, len(nums)):
            complement = target - nums[i]
            if (complement in nums_dict):
                # we do this so we try to get a different index than i - which is growing ascending
                j = nums_dict[complement][-1]
                if (i != j):
                    return [i, j]

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # return self.basic_solution (nums, target)
        return self.map_solution(nums, target)
