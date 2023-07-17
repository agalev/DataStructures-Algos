# https://leetcode.com/problems/shuffle-string/description/
def restoreString(s: str, indices: list[int]) -> str:
    # result = ""
    # hashmap = sorted({indices[i]: s[i] for i in range(len(indices))}.items())
    # sorted_hash = sorted(hashmap.items())
    # for i in sorted_hash:
    #     print(i[1])
    #     result += i[1]
    # return result
    return ''.join([i[1] for i in sorted({indices[i]: s[i] for i in range(len(indices))}.items())])

# Test Cases
print(restoreString("codeleet", [4,5,6,7,0,2,1,3])) # "leetcode"
print(restoreString("abc", [0,1,2])) # "abc"
print(restoreString("aiohn", [3,1,4,2,0])) # "nihao"