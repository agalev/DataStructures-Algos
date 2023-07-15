# https://leetcode.com/problems/create-target-array-in-the-given-order/submissions/
def createTargetArray(nums: list[int], index: list[int]) -> list[int]:
    result = []
    for i in range(len(nums)):
        result.insert(index[i], nums[i])
    return result

# Test Cases
print(createTargetArray([0,1,2,3,4], [0,1,2,2,1])) # [0,4,1,3,2]
print(createTargetArray([1,2,3,4,0], [0,1,2,3,0])) # [0,1,2,3,4]
print(createTargetArray([1], [0])) # [1]