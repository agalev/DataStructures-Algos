# https://leetcode.com/problems/valid-palindrome/
def isPalindrome(s: str) -> bool:
    # initialize a list of all alhpanumeric characters
    AN = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    # initialize a list to store the filtered string
    filtered = []
    # filter the string
    for i in range(len(s)):
        if s[i].lower() in AN:
            filtered.append(s[i].lower())
    left = 0
    right = len(filtered) - 1
    # check if the filtered string is a palindrome
    while left < right:
        if filtered[left] != filtered[right]:
            print(False)
            return False
        left+=1
        right-=1
    print(True)
    return True

isPalindrome("A man, a plan, a canal: Panama") # True