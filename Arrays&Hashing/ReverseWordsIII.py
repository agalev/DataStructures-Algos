# https://leetcode.com/problems/reverse-words-in-a-string-iii/description/
def reverseWords(s: str) -> str:
    return ' '.join([''.join(reversed(list(i))) for i in s.split(' ')])

print(reverseWords("Let's take LeetCode contest")) # "s'teL ekat edoCteeL tsetnoc"
print(reverseWords("God Ding")) # "doG gniD"
print(reverseWords("Hello World")) # "olleH dlroW"