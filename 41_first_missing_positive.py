class Solution:
    def linearMemoryComplexity(self, nums: List[int]) -> int:
        # one way to do it would be to store the positives found in a dictionary and maintain the first missing positive looping through the array. but that doesnt respect the memory complexity
        firstMissingPositive = 1
        positives = {}
        for n in nums:
            if (n <= 0 or n in positives):
                continue
            positives[n] = True
            if (n == firstMissingPositive):
                while (firstMissingPositive in positives):
                    firstMissingPositive += 1
        return firstMissingPositive

    def firstMissingPositive(self, nums: List[int]) -> int:
        # one way to do it but that doesnt respect the time complexity would be to simply sort the array and then find the first missing positive looping through the sorted array (wont implement this one)

        # this solves the problem but doesnt respect the constraint about the constant extra space
        # return self.linearMemoryComplexity (nums)

        # since we have n elements, the first missing positive is between 1 and n + 1
        # we can ignore non positive elements, duplicates and elements larger than the size of the array
        for i in range(len(nums)):
            if (nums[i] <= 0):
                # ignoring all non positive elements (we transform them into the largest result possible)
                nums[i] = len(nums) + 1

        # we know wanna loop throught the array in a way where we can mark the indexes positions that we know the index + 1 element is in the array
        # one way to do it would be to simply create another array to be the marker. But this wont respect the constraint, so we will do it in the nums array. Since there are only positive elements in it, we can mark the elements by making them negative (so negative numbers in the arrays represent that the index of that number exists in the array)
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            if (index < len(nums)):
                # nums[i] exists in the array, so we will flag the element represented by it
                nums[index] = -1 * abs(nums[index])

        # now, we need to loop through the array again. All elements that are negative means that the corresponding (index+1) exists in the list
        for i in range(len(nums)):
            if (nums[i] > 0):
                # it means that we didnt find the number i+1 in the array
                return i + 1
        return len(nums) + 1
