# https://leetcode.com/problems/unique-morse-code-words/description/
def uniqueMorseRepresentations(words: list[str]) -> int:
    hashmap = {
        "a": ".-",
        "b": "-...",
        "c": "-.-.",
        "d": "-..",
        "e": ".",
        "f": "..-.",
        "g": "--.",
        "h":  "....",
        "i": "..",
        "j": ".---",
        "k": "-.-",
        "l": ".-..",
        "m": "--",
        "n": "-.",
        "o": "---",
        "p": ".--.",
        "q": "--.-",
        "r": ".-.",
        "s": "...",
        "t": "-",
        "u": "..-",
        "v": "...-",
        "w": ".--",
        "x": "-..-",
        "y": "-.--",
        "z":"--.."
    }
    result = []
    for i in words:
        temp = ''
        for j in i:
            temp += hashmap[j]
        if temp not in result:
            result.append(temp)
    return len(result)

# Test Cases
print(uniqueMorseRepresentations(["gin", "zen", "gig", "msg"])) # return 2
print(uniqueMorseRepresentations(["a"])) # return 1
print(uniqueMorseRepresentations(["a", "b"])) # return 2
print(uniqueMorseRepresentations(["ab", "cd"])) # return 2
print(uniqueMorseRepresentations(["ab", "cd", "ab"])) # return 2