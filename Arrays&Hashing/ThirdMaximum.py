# https://leetcode.com/problems/third-maximum-number/
def thirdMax(nums: list) -> int:
    nums = sorted(list(set(nums)))
    if (len(nums) < 3):
        return nums[-1]
    else:
        return nums[-3]
    
# Test Cases
print(thirdMax([3,2,1])) # 1
print(thirdMax([1,2])) # 2
print(thirdMax([2,2,3,1])) # 1