# https://leetcode.com/problems/concatenation-of-array/description/
def getConcatenation(nums: list[int]) -> list[int]:
    return [*nums,*nums]

print(getConcatenation([1,2,1])) # [1,2,1,1,2,1]
print(getConcatenation([1,3,2,1])) # [1,3,2,1,1,3,2,1]
print(getConcatenation([1])) # [1,1]