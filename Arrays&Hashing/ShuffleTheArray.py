# https://leetcode.com/problems/shuffle-the-array/description/
def shuffle(nums: list[int], n: int) -> list[int]:
        result = []
        for i in range(0,n):
            result.append(nums[i])
            result.append(nums[i+n])
        return result

# Test Cases
print(shuffle([2,5,1,3,4,7], 3)) # [2,3,5,4,1,7]
print(shuffle([1,2,3,4,4,3,2,1], 4)) # [1,4,2,3,3,2,4,1]
print(shuffle([1,1,2,2], 2)) # [1,2,1,2]