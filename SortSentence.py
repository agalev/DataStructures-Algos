# https://leetcode.com/problems/sorting-the-sentence/description/
def sortSentence(s: str) -> str:
    words = s.split(' ')
    result = list(range(len(words)))

    for i in words:
        result[int(list(i)[-1])-1] = ''.join(list(i)[0:-1])
    return ' '.join(result)

# Test Cases
print(sortSentence('is2 sentence4 This1 a3')) # return 'This is a sentence'
print(sortSentence('Myself2 Me1 I4 and3')) # return 'Me Myself and I'