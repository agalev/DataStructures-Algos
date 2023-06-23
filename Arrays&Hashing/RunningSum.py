# https://leetcode.com/problems/running-sum-of-1d-array/description/
def runningSum(nums: list[int]) -> list[int]:
    result = []
    for n in range(len(nums)):
        if n == 0:
            result.append(nums[n])
        else:
            result.append(nums[n] + result[n-1])
    return result

print(runningSum([1,2,3,4])) # [1,3,6,10]
print(runningSum([1,1,1,1,1])) # [1,2,3,4,5]
print(runningSum([3,1,2,10,1])) # [3,4,6,16,17]