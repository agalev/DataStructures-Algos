# https://leetcode.com/problems/reverse-vowels-of-a-string/submissions/977210054/
def reverseVowels(s: str) -> str:
    array = list(s)
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    left_index = 0
    right_index = len(array)-1
    
    while left_index < right_index:
        if (array[left_index] in vowels and array[right_index] in vowels):
            leftV = array[left_index]
            array[left_index] = array[right_index]
            array[right_index] = leftV
            left_index+=1
            right_index-=1
        elif array[left_index] in vowels:
            right_index-=1
        elif array[right_index] in vowels:
            left_index+=1
        else:
            left_index+=1
            right_index-=1
    return ''.join(array)

print(reverseVowels("hello")) # "holle"
print(reverseVowels("leetcode")) # "leotcede"
print(reverseVowels("aA")) # "Aa"
