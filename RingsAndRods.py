# https://leetcode.com/problems/rings-and-rods/
def countPoints(rings: str) -> int:
    hash_map = {
        '0': '',
        '1': '',
        '2': '',
        '3': '',
        '4': '',
        '5': '',
        '6': '',
        '7': '',
        '8': '',
        '9': '',
    }
    for i in range(0,len(rings) - 1, 2):
        hash_map[rings[i+1]] += rings[i]
    return sum([1 for i in hash_map.values() if 'B' in i and 'G' in i and 'R' in i])

# Test cases
print(countPoints("B0B6G0R6R0R6G9")) # 1
print(countPoints("B0R0G0R9R0B0G0")) # 1
print(countPoints("B0B0B0B0B0B0B0")) # 0
print(countPoints("R9R9R9R9R9R9R9")) # 0
