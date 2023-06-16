# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
def twoSum(numbers: list, target: int) -> list:
    left = 0
    right = len(numbers) - 1
    while left < right:
        if numbers[left] + numbers[right] == target:
            return [left+1, right+1]
        elif numbers[left] + numbers[right] > target:
            right -= 1
        else:
            left += 1

print(twoSum([2,7,11,15], 9)) # [1,2]
print(twoSum([2,3,4], 6)) # [1,3]
print(twoSum([-1,0], -1)) # [1,2]
print(twoSum([0,0,3,4], 0)) # [1,2]
