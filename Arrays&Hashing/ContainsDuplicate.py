# https://leetcode.com/problems/contains-duplicate/
def containsDuplicate(nums) -> bool:
    # initialize a map to store the unique values
    map = {}
    for i in nums:
        if i in map:
            return True
        else:
            map[i] = 1
    return False

print(containsDuplicate([1,2,3,1])) # True