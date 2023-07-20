# https://leetcode.com/problems/number-of-arithmetic-triplets/description/
def arithmeticTriplets(nums: list[int], diff: int) -> int:
    return sum([1 if nums[i] + diff in nums and nums[i] + 2 * diff in nums else 0 for i in range(len(nums))])

# Test Cases
print(arithmeticTriplets([1,2,3,4], 1)) # 3
print(arithmeticTriplets([1,3,5,7,9], 3)) # 5
print(arithmeticTriplets([1,1,1,1,1], 0)) # 1