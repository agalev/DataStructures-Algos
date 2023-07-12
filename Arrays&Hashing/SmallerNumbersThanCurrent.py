# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/description/
def smallerNumbersThanCurrent(nums: list[int]) -> list[int]:
    return([sum([1 for j in nums if i > j]) for i in nums])

# Test Cases
print(smallerNumbersThanCurrent([8,1,2,2,3])) # [4,0,1,1,3]
print(smallerNumbersThanCurrent([6,5,4,8])) # [2,1,0,3]
print(smallerNumbersThanCurrent([7,7,7,7])) # [0,0,0,0]