# https://leetcode.com/problems/build-array-from-permutation/description/
def buildArray(nums: list[int]) -> list[int]:
        return [nums[nums[i]] for i in range(len(nums))]

# Test Cases
print(buildArray([0,2,1,5,3,4])) # [0,1,2,4,5,3]
print(buildArray([5,0,1,2,3,4])) # [4,5,0,1,2,3]