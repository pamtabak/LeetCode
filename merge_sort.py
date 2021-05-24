def merge_sort(nums):
    if (len(nums) == 1):
        return nums

    mid = len(nums) // 2
    left_half = nums[0:mid]
    right_half = nums[mid:]

    merge_sort(left_half)
    merge_sort(right_half)

    i = 0
    j = 0
    k = 0

    while (i < len(left_half) and j < len(right_half)):
        if (left_half[i] < right_half[j]):
            nums[k] = left_half[i]
            i += 1
        else:
            nums[k] = right_half[j]
            j += 1
        k += 1

    while (i < len(left_half)):
        nums[k] = left_half[i]
        i += 1
        k += 1

    while (j < len(right_half)):
        nums[k] = right_half[j]
        j += 1
        k += 1
    return nums


print(merge_sort([1, 2, 3, 4, 1, 2, 3, 9, 1, 2, -1, 0, 2]))
