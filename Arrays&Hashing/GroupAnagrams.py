# https://leetcode.com/problems/group-anagrams/description/
def groupAnagrams(strs: list[str]) -> list[list[str]]:
    map = {}
    result = []
    result_index = 0
    for i in strs:
        if ''.join(sorted(i)) not in map:
            map[''.join(sorted(i))] = result_index
            result_index += 1
            result.append([i])
        else:
            result[map[''.join(sorted(i))]].append(i)
    return result

# Test Cases
print(groupAnagrams(["eat","tea","tan","ate","nat","bat"])) # [["bat"],["nat","tan"],["ate","eat","tea"]]
print(groupAnagrams([""])) # [[""]]
print(groupAnagrams(["a"])) # [["a"]]
print(groupAnagrams(["cab","tin","pew","duh","may","ill","buy","bar","max","doc", "bac"])) # [["doc"],["bar"],["buy"],["ill"],["may"],["tin"],["cab", "bac",],["pew"],["max"],["duh"]]