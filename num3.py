def contains_duplicate(nums):
    return len(nums) != len(set(nums))
nums1 = [1, 2, 3, 4]
print(contains_duplicate(nums1))

nums2 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
print(contains_duplicate(nums2))

nums3 = [1, 2, 3, 1]
print(contains_duplicate(nums3))
