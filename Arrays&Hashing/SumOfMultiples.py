# https://leetcode.com/problems/sum-multiples/description/
def sumOfMultiples(n: int) -> int:
    return sum([i for i in range(1,n+1) if i%3 == 0 or i%5 == 0 or i%7 == 0])

# Test Cases
print(sumOfMultiples(10)) # 40
print(sumOfMultiples(15)) # 81
print(sumOfMultiples(20)) # 119

# scratch paper
# array = [1,2,3,4]
# print({a:b for a,b in enumerate(array)})