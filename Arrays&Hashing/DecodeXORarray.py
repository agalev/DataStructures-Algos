# https://leetcode.com/problems/decode-xored-array/description/
def decode(encoded: list[int], first: int) -> list[int]:
    r = [first]
    for i in encoded:
        r.append(r[-1]^i)
    return r

# Test Cases
print(decode([1,2,3], 1)) # [1,0,2,1]
print(decode([6,2,7,3], 4)) # [4,2,0,7,4]
