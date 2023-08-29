# For a given string, output "x" for each unique character, otherwise output 'y' for each duplicate character.
# Return the same structure of the string. E.g. "hello" -> "xxyyx"
# Given by FDM Group

def XYstring(string: str) -> str:
    hashmap = {}
    for i in string:
        if i not in hashmap:
            hashmap[i] = 1
        else:
            hashmap[i] += 1
    for i in string:
        if hashmap[i] > 1:
            string = string.replace(i, "y")
        else:
            string = string.replace(i, "x")
    return string

print(XYstring("hello")) # xxyyx
print(XYstring("a")) # x
print(XYstring("ab")) # xy
print(XYstring("aa")) # yy