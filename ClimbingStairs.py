# https://leetcode.com/problems/climbing-stairs/description/
def climbStairs(n: int) -> int:
    prev, prev2 = 0, 1
    for i in range(n):
        prev, prev2 = prev2, prev + prev2
    return prev2

print(climbStairs(2)) # 2
print(climbStairs(3)) # 3
print(climbStairs(4)) # 5
print(climbStairs(5)) # 8
print(climbStairs(6)) # 13
print(climbStairs(7)) # 21
print(climbStairs(8)) # 34
print(climbStairs(9)) # 55
print(climbStairs(10)) # 89