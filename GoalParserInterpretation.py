# https://leetcode.com/problems/goal-parser-interpretation/description/
def interpret(command: str) -> str:
        result = ''
        pointer = 0
        while pointer < len(command):
            if command[pointer:pointer+4] == '(al)':
                pointer += 4
                result += 'al'
            elif command[pointer:pointer+2] == '()':
                pointer += 2
                result += 'o'
            else:
                pointer += 1
                result += 'G'
        return result

# Test Cases
print(interpret('G()(al)')) # return 'Goal'
print(interpret('G()()()()(al)')) # return 'Gooooal'
print(interpret('(al)G(al)()()G')) # return 'alGalooG'