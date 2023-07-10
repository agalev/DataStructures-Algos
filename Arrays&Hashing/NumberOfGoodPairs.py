# https://leetcode.com/problems/number-of-good-pairs/description/
def numIdenticalPairs(nums: list[int]) -> int:
    result = 0
    left_index = 0
    right_index = len(nums) - 1

    while left_index < len(nums) - 1:
        if left_index == right_index:
            left_index += 1
            right_index = len(nums) - 1
            continue
        elif nums[left_index] == nums[right_index]:
            result += 1
        right_index -= 1
    
    return result

# Test Cases
print(numIdenticalPairs([1,2,3,1,1,3])) # 4
print(numIdenticalPairs([1,1,1,1])) # 6
print(numIdenticalPairs([1,2,3])) # 0
