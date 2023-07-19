# https://leetcode.com/problems/truncate-sentence/submissions/
def truncateSentence(s: str, k: int) -> str:
    return ' '.join(s.split(' ')[0:k])

# Test Cases
print(truncateSentence("Hello how are you Contestant", 4)) # "Hello how are you"
print(truncateSentence("What is the solution to this problem", 4)) # "What is the solution"
print(truncateSentence("chopper is not a tanuki", 5)) # "chopper is not a tanuki"