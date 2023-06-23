# https://leetcode.com/problems/find-pivot-index/description/
# Notes: Not the most efficient solution, but it works. I think it's O(n^2) time complexity.
# def pivotIndex(nums: list[int]) -> int:
#     for i in range(len(nums)):
#         left_sum = 0
#         right_sum = 0
#         if i == 0:
#             for j in range(1,len(nums)):
#                 right_sum += nums[j]
#         elif i == len(nums):
#             for j in range(0, len(nums)):
#                 left_sum += nums[j]
#         else:
#             for left_index in range(0, i):
#                 left_sum += nums[left_index]
#             for right_index in range(i+1, len(nums)):
#                 right_sum += nums[right_index]
#         if left_sum == right_sum:
#             return i
#     return -1

# Notes: This is a more efficient solution implementing SUM on array and it passes all the testcases on leetcode.
# def pivotIndex(nums: list[int]) -> int:
#         for i in range(len(nums)):
#             left_sum = 0
#             right_sum = 0
#             if i == 0:
#                     right_sum = sum(nums[1:])
#             elif i == len(nums):
#                     left_sum = sum(nums[:1])
#             else:
#                 left_sum = sum(nums[:i])
#                 right_sum = sum(nums[i+1:])
#             if left_sum == right_sum:
#                 return i
#         return -1

# Notes: This is the most efficient solution I discovered from the Solutions section. It's O(n) time complexity.
def pivotIndex(nums: list[int]) -> int:
    leftSum, rightSum = 0, sum(nums)
    for index, element in enumerate(nums):
        rightSum -= element
        if leftSum == rightSum:
            return index
        leftSum += element
    return -1


print(pivotIndex([1,7,3,6,5,6])) # 3
print(pivotIndex([1,2,3])) # -1
print(pivotIndex([2,1,-1])) # 0
print(pivotIndex([1,2,3,4,5,6,7,8,9,10])) # -1