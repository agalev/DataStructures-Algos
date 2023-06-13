# https://leetcode.com/problems/search-insert-position/description/
def searchInsert(nums: list, target: int) -> int:
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = int((left+right) / 2)
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            return mid
    return left

print(searchInsert([1,3,5,6], 5)) # 2
print(searchInsert([1,3,5,6], 2)) # 1
print(searchInsert([1,3,5,6], 7)) # 4