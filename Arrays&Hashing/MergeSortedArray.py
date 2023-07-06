def merge(nums1: list[int], nums2: list[int]) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    indexer = 0
    for i in nums2:
        nums1[len(nums1) - len(nums2) + indexer] = i
        indexer += 1
    nums1.sort()

# Test Cases
nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
merge(nums1, nums2)
print(nums1) # [1,2,2,3,5,6]