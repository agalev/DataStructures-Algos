# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
def findMin(nums: list[int]) -> int:
        leftIndex, rightIndex = 0, len(nums) - 1
        while leftIndex < rightIndex:
            mid = (leftIndex + rightIndex) // 2
            if nums[mid] > nums[rightIndex]:
                leftIndex = mid + 1
            else:
                rightIndex = mid
        return nums[leftIndex]

print(findMin([3,4,5,1,2])) # 1
print(findMin([4,5,6,7,0,1,2])) # 0
print(findMin([11,13,15,17])) # 11
print(findMin([2,1])) # 1
print(findMin([1])) # 1
print(findMin([1,2,3,4,5,6,7])) # 1
print(findMin([2,3,4,5,6,7,1])) # 1
print(findMin([3,4,5,6,7,1,2])) # 1