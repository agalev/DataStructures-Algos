# https://leetcode.com/problems/jewels-and-stones/description/
def numJewelsInStones(jewels: str, stones: str) -> int:
        return sum([1 if i in list(jewels) else 0 for i in list(stones)])

# Test Cases
print(numJewelsInStones('aA', 'aAAbbbb')) # return 3
print(numJewelsInStones('z', 'ZZ')) # return 0
