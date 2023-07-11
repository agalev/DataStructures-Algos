# https://leetcode.com/problems/left-and-right-sum-differences/description/
def leftRightDifference(nums: list[int]) -> list[int]:
    # answer = []
    # for i in range(len(nums)):
    #     to_append = abs(sum(nums[0:i]) - sum(nums[i+1:]))
    
    return [abs(sum(nums[0:i]) - sum(nums[i+1:])) for i in range(len(nums))]

# Test Cases
print(leftRightDifference([2,3,5,1,3])) # [12, 7, 1, 7, 11]
print(leftRightDifference([4,2,1,1,2])) # [6, 0, 3, 5, 8]
print(leftRightDifference([12,1,12])) # [13, 0, 13]
print(leftRightDifference([1,2,3,4])) # [9, 6, 1, 6]