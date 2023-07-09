# https://leetcode.com/problems/final-value-of-variable-after-performing-operations/description/
def finalValueAfterOperations(operations: list[str]) -> int:
    hashmap = {
        "++X": 1,
        "X++": 1,
        "--X": -1,
        "X--": -1,
    }
    return sum([hashmap[i] for i in operations])

# Test Cases
print(finalValueAfterOperations(["--X","X++","X++"])) # 1
print(finalValueAfterOperations(["++X","++X","X++"])) # 3
print(finalValueAfterOperations(["X++","++X","--X","X--"])) # 0