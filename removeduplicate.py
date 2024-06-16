def removeDuplicates(nums):
    if not nums:
        return 0

    k = 1  # Pointer for the next unique element
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[k] = nums[i]
            k += 1
    return k

nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2  # Note: val is not used in this problem
# Sort the array first since the problem assumes a sorted array
nums.sort()
k = removeDuplicates(nums)
print(k)  # Output: 5 (since the sorted array will be [0, 0, 1, 2, 2, 2, 3, 4])
print(nums[:k])  # Output: [0, 1, 2, 3, 4]