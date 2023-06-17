# https://leetcode.com/problems/missing-number/description/
def missingNumber(nums: list) -> int:
    nums.sort()
    for i in range(len(nums)):
        if i != nums[i]:
            return i
    return nums[-1]+1

print(missingNumber([3,0,1])) # 2
print(missingNumber([9,6,4,2,3,5,7,0,1])) # 8
print(missingNumber([0])) # 1
print(missingNumber([0,1])) # 2
print(missingNumber([1])) # 0
print(missingNumber([1,2])) # 0