def intersection(nums1, nums2):
    same = []
    for i in nums1:
        if i in nums2:
            same.append(i)
    return same
    
print(intersection([4, 9, 5], [9, 4, 9, 8, 4]))
print(intersection([4, 5], [9, 4, 9, 8, 4]))