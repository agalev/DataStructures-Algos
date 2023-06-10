# https://leetcode.com/problems/contains-duplicate/
def containsDuplicate(nums) -> bool:
    # initialize a map to store the unique values
    map = {}
    for i in nums:
        if i in map:
            print(True)
            return True
        else:
            map[i] = 1
    print(False)
    return False

containsDuplicate([1,2,3,1]) # True