# https://leetcode.com/problems/number-of-employees-who-met-the-target/
def numberOfEmployeesWhoMetTarget(hours: list, target: int) -> int:
    result = 0
    for i in hours:
        if i >= target:
            result += 1
    return result

# Test cases
print(numberOfEmployeesWhoMetTarget([1,2,3,4,5], 3)) # 3
print(numberOfEmployeesWhoMetTarget([2,3,5,6], 5)) # 2