def merge_two_sorted_array(nums1, m, nums2, n):
    temp1= nums1[:3]
    nums1[:m+n]= temp1+ nums2
    return nums1


nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
result= merge_two_sorted_array(nums1, m, nums2, n)
print(result)