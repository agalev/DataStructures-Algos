# https://leetcode.com/problems/3sum/description/
def threeSum(nums: list[int]) -> list[list[int]]:
    result = []
    nums.sort()

    for index, element in enumerate(nums):
        if index > 0 and nums[index] == nums[index-1]:
            continue
        left_index = index + 1
        right_index = len(nums) - 1
        while left_index < right_index:
            threesum = element + nums[left_index] + nums[right_index]
            if threesum == 0:
                result.append([element, nums[left_index], nums[right_index]])
                left_index += 1
                while left_index < right_index and nums[left_index] == nums[left_index-1]:
                    left_index +=1
            elif threesum > 0:
                right_index -= 1
            else:
                left_index += 1
    return result

# Test Cases
print(threeSum([-1,0,1,2,-1,-4])) # [[-1,-1,2],[-1,0,1]]
print(threeSum([])) # []
print(threeSum([0])) # []
print(threeSum([0,0,0])) # [[0,0,0]]
