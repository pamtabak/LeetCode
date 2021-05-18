class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # the first thing we have to do is concat both arrays maintaing the order
        nums = []
        index1 = 0
        index2 = 0
        while (index1 != len(nums1) or index2 != len(nums2)):
            if (index1 == len(nums1)):
                nums.append(nums2[index2])
                index2 += 1
            elif (index2 == len(nums2)):
                nums.append(nums1[index1])
                index1 += 1
            elif (nums1[index1] <= nums2[index2]):
                nums.append(nums1[index1])
                index1 += 1
            else:
                nums.append(nums2[index2])
                index2 += 1
        # get the median
        print(nums)
        median = float(nums[len(nums)//2])
        if (len(nums) % 2 == 0):
            median += float(nums[int(len(nums)/2 - 1)])
            median = median/2
        return median
