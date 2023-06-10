# https://leetcode.com/problems/two-sum/
def twoSum(nums, target: int):
    map = {}
    for i in range(len(nums)):
        if nums[i] in map.values():
            return [i, list(map.values()).index(nums[i])]
        map[i] = target - nums[i]

print(twoSum([2,7,11,15], 9)) # [0,1]