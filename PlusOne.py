# https://leetcode.com/problems/plus-one/description/
def plusOne(digits: list) -> list:
        nums = ''
        result = []
        for i in digits:
            nums += str(i)
        nums = int(nums) + 1
        return [int(num) for num in str(nums)]

print(plusOne([1,2,3])) # [1,2,4]
print(plusOne([4,3,2,1])) # [4,3,2,2]
print(plusOne([0])) # [1]