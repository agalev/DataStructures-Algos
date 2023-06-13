# https://leetcode.com/problems/remove-element/description/
# Given an array nums and a value val, remove all instances of that value in-place and return the new length.
def removeElement(nums: list, val: int) -> int:
    i = len(nums) - 1
    while i >= 0:
        if nums[i] == val:
            nums.pop(i)
        i -= 1
    return len(nums)

print(removeElement([3,2,2,3], 3)) # 2, nums = [2,2]
print(removeElement([0,1,2,2,3,0,4,2], 2)) # 5, nums = [0,1,4,0,3]