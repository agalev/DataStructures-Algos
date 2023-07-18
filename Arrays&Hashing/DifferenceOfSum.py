# https://leetcode.com/problems/difference-between-element-sum-and-digit-sum-of-an-array/description/
def differenceOfSum(nums: list[int]) -> int:
        el_sum = sum(nums)
        dig_sum = []
        for i in nums:
            for j in list(str(i)):
                dig_sum.append(int(j))
        return abs(el_sum - sum(dig_sum))

# Test Cases
print(differenceOfSum([123, 45, 6789])) # 6912
print(differenceOfSum([100, 2, 3, 4, 5])) # 99
print(differenceOfSum([1, 2, 3, 4, 5])) # 0