# https://leetcode.com/problems/richest-customer-wealth/description/
def maximumWealth(accounts: list[list[int]]) -> int:
    return max([sum(i) for i in accounts])

# Test Cases
print(maximumWealth([[1,2,3],[3,2,1]])) # 6
print(maximumWealth([[1,5],[7,3],[3,5]])) # 10
print(maximumWealth([[2,8,7],[7,1,3],[1,9,5]])) # 17
