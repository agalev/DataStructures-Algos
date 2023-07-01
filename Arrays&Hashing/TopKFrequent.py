# https://leetcode.com/problems/top-k-frequent-elements/description/
def topKFrequent(nums: list[int], k: int) -> list[int]:
        map = {}
        for i in nums:
            if i not in map:
                map[i] = 1
            else:
                map[i] += 1
        sorted_by_frequence = sorted(map.items(), key = lambda x: x[1], reverse = True)
        return [sorted_by_frequence[i][0] for i in range(k)]

# Test Cases
print(topKFrequent([1,1,1,2,2,3], 2)) # [1,2]
print(topKFrequent([1], 1)) # [1]
print(topKFrequent([1,2], 2)) # [1,2]
print(topKFrequent([1,2,2,3,3,3], 1)) # [3]
print(topKFrequent([1,2,2,3,3,3], 2)) # [3,2]