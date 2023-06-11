# https://leetcode.com/problems/reverse-integer/
# Given a 32-bit signed integer, reverse digits of an integer.
def reverse(x: int) -> int:
    array = list(str(x))
    result = []
    if array[0] == '-':
        result.append(array[0])
        while (len(array) - 1):
            result.append(array.pop())
    else:
        while len(array):
            result.append(array.pop())
    if (int("".join(result)) > 2147483647 or
        int("".join(result)) < -2147483647):
        return 0
    else:
        return int("".join(result))
    
print(reverse(123)) # 321
print(reverse(-123)) # -321
print(reverse(120)) # 21