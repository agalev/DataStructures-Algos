# https://leetcode.com/problems/decompress-run-length-encoded-list/description/
def decompressRLElist(nums: list[int]) -> list[int]:
    result = []
    for i in range(0, len(nums), 2):
        repeater = nums[i]
        value = nums[i+1]
        result += [value] * repeater
    return result

# Test Cases
print(decompressRLElist([1,2,3,4])) # [2,4,4,4]
print(decompressRLElist([1,1,2,3])) # [1,3,3]
print(decompressRLElist([1,1,1,1])) # [1, 1]
