# https://leetcode.com/problems/shifting-letters-ii/description/
# This solution is O(n^2) time complexity and does not pass all test cases
def shiftingLetters(s: str, shifts: list[list[int]]) -> str:
        list_map = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        string_listed = list(s)
        for i in range(len(shifts)):
            for j in range(shifts[i][0], shifts[i][1]+1):
                if string_listed[j] == 'z' and shifts[i][2] == 1:
                    string_listed[j] = 'a'
                elif string_listed[j] == 'a' and shifts[i][2] == 0:
                    string_listed[j] = 'z'
                elif shifts[i][2] == 1:
                    string_listed[j] = list_map[list_map.index(string_listed[j])+1]
                elif shifts[i][2] == 0:
                    string_listed[j] = list_map[list_map.index(string_listed[j])-1]
        return ''.join(string_listed)

# Test Cases
print(shiftingLetters('abc', [[0,1,0],[1,2,1],[0,2,1]])) # return 'ace'
print(shiftingLetters('dztz', [[0,0,0],[1,1,1]])) # return 'aab'