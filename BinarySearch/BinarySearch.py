# https://leetcode.com/problems/binary-search/description/
def search(nums: list, target: int) -> int:
    if nums[0] == target:
        return 0
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = int((left+right) / 2)
        if target < nums[mid]:
            right = mid - 1
        elif target > nums[mid]:
            left = mid + 1
        else:
            return mid
    return -1

print(search([1,2,3,4,5,6,7,8,9,10], 5)) # 4
print(search([-1,0,3,5,9,12], 9)) # 4
print(search([-1,0,3,5,9,12], 2)) # -1
print(search([5], 5)) # 0
print(search([2,5], 5)) # 1
print(search([2,5], 2)) # 0