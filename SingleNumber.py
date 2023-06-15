# https://leetcode.com/problems/single-number/description/
def singleNumber(nums: list) -> int:
    result = 0
    for i in nums:
        result = result^i
    return result

print(singleNumber([2,2,1])) # 1
print(singleNumber([4,1,2,1,2])) # 4
print(singleNumber([1])) # 1
print(singleNumber([1,1,2,2,3,3,4,4,5])) # 5